# load environment variable
from dotenv import load_dotenv

load_dotenv()

# standard library
import logging

# 3rd party library
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS

# local module
from src.constants import PATH
from src.shared_types import FrontCardData, TranslateAPIResponse, QuestionAPIResponse
from src.image.card_image import CardImage
from src.image.user_image import UserImage
from src.card.translation import TranslationPipeline, normalize_punctuation
from src.card.text_extractor import OcrTextExtractor
from src.card.translator import YugiohTranslator


# app
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

    # 使用者上傳圖片在這裡
    image = request.files["image"]

    # 儲存圖片
    user_image = UserImage(image)
    user_image.save()

    # 將圖片上傳到 Imgur，並回傳圖片 URL
    user_image_url = user_image.create_url()

    # 翻譯圖片
    translated_text = translation_pipeline.process(user_image_url)

    # 文字翻譯，產出 FrontCardData
    front_card_data: FrontCardData = {"description": translated_text}

    # 刪除圖片
    user_image.remove()

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
        "answer": f"嗯...我知道你問了「{question_text}」，但拍謝，問答功能還在開發中噢！",
    }

    return jsonify(response)


# 卡片材質 API
@app.route("/api/assets/card-material/<path:filepath>")
def serve_card_material(filepath: str):
    return send_from_directory(PATH.YUGIOH_MATERIAL_DIR.value, filepath)


# 卡面圖片 API
@app.route("/api/assets/card-image/<image_id>")
def serve_card_image(image_id: str):
    
    # 卡面圖片
    card_image = CardImage(image_id, logger=logger)

    # 如果不存在就下載
    if not card_image.exists_locally():
        card_image.download()

    return send_file(card_image.local_path)

if __name__ == "__main__":
    # 日誌
    logger = app.logger
    logger.setLevel(logging.DEBUG)

    # OCR 文字提取器
    text_extractor = OcrTextExtractor(logger=logger)

    # 翻譯模型
    translator = YugiohTranslator(logger=logger)

    # 翻譯管線
    translation_pipeline = TranslationPipeline(text_extractor, translator)
    translation_pipeline.add_postprocess_hook(normalize_punctuation)

    # 在 DEBUG 模式時，整個代碼會再重複執行一次
    app.run(debug=True, port=3000)
