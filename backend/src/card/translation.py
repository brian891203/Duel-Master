# standrad library
import logging
import re
import time
import json
from base64 import b64encode

# 3rd party library
import requests
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

# local module
from . import tokenizer, model, device
from src.constants import API
from src.shared_types import FrontCardData
from src.utils.misc import try_getenv


def translate_sentence(
    sentence,
    top_k: int = 50,
    max_length: int = 128,
    top_p: float = 0.95,
    temperature: float = 0.1,
    num_return_sequences: int = 1,
):
    """
    文字翻譯
    """
    return model.generate(
        sentence,
        do_sample=True,
        top_k=top_k,
        max_length=max_length,
        top_p=top_p,
        temperature=temperature,
        num_return_sequences=num_return_sequences,
    )


def translate_paragraph_not_split(
    paragraph,
    top_k: int = 50,
    max_length: int = 768,
    top_p: float = 0.95,
    temperature: float = 0.1,
    num_return_sequences: int = 1,
):
    """
    翻譯主功能
    """
    prefix = "<-ja2zh->"

    encodings_text = tokenizer.encode(
        prefix + paragraph,
        return_tensors="pt",
        max_length=max_length,
        padding="max_length",
        truncation=True,
    ).to(device)

    output = translate_sentence(
        encodings_text,
        top_k=top_k,
        max_length=max_length,
        top_p=top_p,
        temperature=temperature,
        num_return_sequences=num_return_sequences,
    )

    translated = [tokenizer.decode(o, skip_special_tokens=True) for o in output]

    return translated[0]


def image_create_url(
    image_path: str,
    file_name: str,
    *,
    logger: logging.Logger,
) -> str:
    """
    將圖片上傳到 Imgur，並回傳圖片 URL
    """
    api_key = try_getenv("IMGUR_API_KEY")
    client_id = try_getenv("IMGUR_CLIENT_ID")

    j1 = requests.post(
        API.IMGUR.value,
        headers={"Authorization": f"Client-ID {client_id}"},
        data={
            "key": api_key,
            "image": b64encode(open(image_path, "rb").read()),
            "type": "base64",
            "name": file_name,
            "title": file_name,
        },
    )

    responses = json.loads(j1.text)
    url = responses["data"]["link"]
    logger.info(url)

    return url


def extract_text_from_image(
    read_image_url: str, *, logger: logging.Logger
) -> list[str]:
    """
    處理圖片，轉成文字 (OCR)
    """
    trans_text = []

    subscription_key = try_getenv("AZURE_CV_SUBSCRIPTION_KEY")
    endpoint = try_getenv("AZURE_CV_ENDPOINT")

    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(subscription_key)
    )

    # OCR: Read File using the Read API, extract text - remote
    # This example will extract text in an image, then print results, line by line.
    # This API call can also extract handwriting style text (not shown).

    logger.info("===== Read File - remote =====")

    read_response = computervision_client.read(read_image_url, raw=True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ["notStarted", "running"]:
            break
        time.sleep(1)

    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                trans_text.append(line.text)

    logger.info(trans_text)

    return trans_text


def create_front_card_data(text_list: list[str]) -> FrontCardData:
    """
    文字翻譯，產出 FrontCardData
    """
    trans_text = ""
    for line in text_list:
        if re.match(r"^[A-Z0-9]+[\- ][A-Z0-9]+", line):
            continue
        if re.match(r"[0-9]{8}", line):
            break
        if "ATK" in line or "DEF" in line:
            break
        trans_text += line
        trans_text += "\n"

    # 翻譯
    trans_result = translate_paragraph_not_split(trans_text)

    # 後處理
    norm_map = {
        ":": "：",
        ";": "；",
        "!": "！",
        "?": "？",
        ",": "，",
        ".": "。",
    }
    trans_result = "".join(norm_map.get(char, char) for char in trans_result)

    return {"description": trans_result}
