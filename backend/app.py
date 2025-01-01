# standard library
import os

# 3rd party library
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS

# local module
from src.constants import PATH
from src.shared_types import TranslateAPIResponse, QuestionAPIResponse
from src.card.image import get_card_image_path, download_card_image
from src.card.translation import (
    image_create_url,
    extract_text_from_image,
    create_front_card_data,
)


app = Flask(__name__)
CORS(app)


# 翻譯 API
@app.route("/api/translate", methods=["POST"])
def translate_api():

    if "image" not in request.files:
        response: TranslateAPIResponse = {
            "success": False,
            "errMessage": "No image file provided",
        }
        return jsonify(response), 400

    # 圖片在這裡
    image = request.files["image"]
    image_path = f"{PATH.USER_UPLOAD_IMAGE_DIR.value}/{image.filename}"

    # 儲存檔案
    image.save(image_path)

    # 將圖片上傳到 Imgur，並回傳圖片 URL
    url = image_create_url(image_path, image.filename, logger=app.logger)

    # 處理圖片，轉成文字 (OCR)
    jp_text_list = extract_text_from_image(url, logger=app.logger)

    # 文字翻譯，產出 FrontCardData
    front_card_data = create_front_card_data(jp_text_list)

    # 刪除圖片檔
    if os.path.exists(image_path):
        os.remove(image_path)
        app.logger.info(f"Image {image_path} has been deleted!")

    # 產生 response
    response: TranslateAPIResponse = {
        "success": True,
        "frontCardData": front_card_data,
    }

    return jsonify(response)


# 問答 API
@app.route("/api/question", methods=["POST"])
def question_api():
    if not request.data:
        response: QuestionAPIResponse = {
            "success": False,
            "errMessage": "No question text provided",
        }
        return jsonify(response), 400

    # 問題在這裡
    question_text = request.data.decode("utf-8")

    response: QuestionAPIResponse = {
        "success": True,
        "answer": f"Your question '{question_text}' has been successfully processed.",
    }

    return jsonify(response)


# 卡片材質 API
@app.route("/api/assets/card-material/<path:filepath>")
def serve_card_material(filepath: str):
    return send_from_directory(PATH.YUGIOH_MATERIAL_DIR.value, filepath)


# 卡片圖片 API
@app.route("/api/assets/card-image/<image_id>")
def serve_card_image(image_id: str):
    image_path = get_card_image_path(image_id)

    # 如果圖片不存在，就下載圖片
    if not os.path.exists(image_path):
        download_card_image(image_id, image_path, logger=app.logger)

    return send_file(image_path)


if __name__ == "__main__":
    app.run(port=3000)
    # 在 DEBUG 模式時，整個代碼會再重複執行一次
