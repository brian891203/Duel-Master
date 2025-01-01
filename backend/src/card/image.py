# standard library
import os
import logging

# 3rd party library
import requests

# local module
from src.constants import API, PATH


def get_card_image_path(
    card_id: str | None = None,
) -> str:
    """
    有 ID 時，回傳圖片路徑；沒有 ID 時，回傳目錄路徑
    """

    if card_id:
        return f"{PATH.YUGIOH_IMAGE_DIR.value}/{card_id}.jpg"
    return PATH.YUGIOH_IMAGE_DIR.value


def download_card_image(
    card_id: str,
    download_path: str | os.PathLike[str],
    *,
    logger: logging.Logger,
) -> None:
    """
    下載 YUGIOH 卡片圖片
    """

    try:
        image_url = f"{API.YUGIOH_IMAGE.value}/{card_id}.jpg"
        response = requests.get(image_url)  # 下載圖片
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading image. Error Message - {e}")
    else:
        if response.status_code == 200:
            with open(download_path, "wb") as file:
                file.write(response.content)  # 將圖片寫入檔案
