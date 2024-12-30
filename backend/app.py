# standard library
import os

# 3rd party library
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS

# local module
from src.shared_types import TranslateAPIResponse, QuestionAPIResponse, FrontCardData
from src.utils import download_card_image, card_image_path
from src.constants import PATH


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

    image = request.files["image"]  # 圖片在這裡

    mock_front_card_data: FrontCardData = {
        "name": "灰流麗",
        "attribute": "fire",
        "level": 3,
        "monsterType": "不死族",
        "atk": 0,
        "def": 1800,
        "description": "「灰流麗」的效果1回合僅能使用1次。 包含以下效果的魔法、陷阱、怪獸效果發動時，可以從手札捨棄此卡發動。該效果無效。此效果也可以在對手回合發動。 ●從牌組將卡片加入手札的效果●從牌組將怪獸特殊召喚的效果●從牌組將卡片送入墓地的效果",
    }

    response: TranslateAPIResponse = {
        "success": True,
        "frontCardData": mock_front_card_data,
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

    question_text = request.data.decode("utf-8")  # 問題在這裡

    response: QuestionAPIResponse = {
        "success": True,
        "answer": f"Your question '{question_text}' has been successfully processed.",
    }

    return jsonify(response)


# 卡片材質包路由
@app.route("/api/assets/card-material/<path:filepath>")
def serve_card_material(filepath: str):
    return send_from_directory(PATH.YUGIOH_MATERIAL_DIR.value, filepath)


# 卡片圖片路由
@app.route("/api/assets/card-image/<image_id>")
def serve_card_image(image_id: str):
    image_path = card_image_path(image_id)

    # 如果圖片不存在，就下載圖片
    if not os.path.exists(image_path):
        download_card_image(image_id, image_path, logger=app.logger)

    return send_file(image_path)


if __name__ == "__main__":
    app.run(debug=True, port=3000)  # ! debug
