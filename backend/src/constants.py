from enum import Enum

class API(Enum):
    YUGIOH_IMAGE = "https://images.ygoprodeck.com/images/cards_cropped"


class PATH(Enum):
    YUGIOH_IMAGE_DIR = "./assets/card-image"
    YUGIOH_MATERIAL_DIR = "./assets/yugioh-card"
