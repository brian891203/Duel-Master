from typing import Literal, TypedDict

# Enums (FRONT)
Language = Literal["sc", "tc", "jp", "kr", "en", "astral"]  # ! Only keep "sc"
Font = Literal["custom1", "custom2", ""]  # ! Only keep "custom2" and ""
Align = Literal["left", "center", "right", ""]
Type = Literal["monster", "spell", "trap", "pendulum"]
Attribute = Literal["dark", "light", "earth", "water", "fire", "wind", "divine", ""]
Icon = Literal["equip", "field", "quick-play", "ritual", "continuous", "counter", ""]
CardType = Literal["normal", "effect", "ritual", "fusion", "synchro", "xyz", "link", "token"]
PendulumType = Literal[
    "normal-pendulum",
    "effect-pendulum",
    "ritual-pendulum",
    "fusion-pendulum",
    "synchro-pendulum",
    "xyz-pendulum",
]
ArrowType = Literal[1, 2, 3, 4, 5, 6, 7, 8]  # Directions
Copyright = Literal["sc", "jp", "en", ""]
Laser = Literal["laser1", "laser2", "laser3", "laser4", ""]
Rare = Literal["dt", "ur", "gr", "hr", "ser", "gser", "pser", ""]

# Enums (BACK)
BackType = Literal["normal", "tormentor", "sky-dragon", "winged-dragon"]
Logo = Literal["ocg", "tcg", "rd"]


class CardData(TypedDict, total=False):
    radius: bool
    scale: float


FrontCardData = TypedDict(
    "FrontCardData",
    {
        "language": Language,
        "font": Font,
        "name": str,
        "color": str,
        "align": Align,
        "gradient": bool,
        "gradientColor1": str,
        "gradientColor2": str,
        "type": Type,
        "attribute": Attribute,
        "icon": Icon,
        "image": str,
        "cardType": CardType,
        "pendulumType": PendulumType,
        "level": int,
        "rank": int,
        "pendulumScale": int,
        "pendulumDescription": str,
        "monsterType": str,
        "atkBar": bool,
        "atk": int,
        "def": int,
        "arrowList": list[ArrowType],
        "description": str,
        "firstLineCompress": bool,
        "descriptionAlign": bool,
        "descriptionZoom": float,
        "descriptionWeight": float,
        "package": str,
        "password": str,
        "copyright": Copyright,
        "laser": Laser,
        "rare": Rare,
        "twentieth": bool,
        "radius": bool,
        "scale": float,
    },
    total=False,
)


class BackCardData(TypedDict, total=False):
    type: BackType
    logo: Logo
    konami: bool
    register: bool
    radius: bool
    scale: float


# TranslateAPIResponse
class TranslateSuccessResponse(TypedDict):
    success: Literal[True]
    frontCardData: FrontCardData


class TranslateFailureResponse(TypedDict):
    success: Literal[False]
    errMessage: str


TranslateAPIResponse = TranslateSuccessResponse | TranslateFailureResponse


# QuestionAPIResponse
class QuestionSuccessResponse(TypedDict):
    success: Literal[True]
    answer: str


class QuestionFailureResponse(TypedDict):
    success: Literal[False]
    errMessage: str


QuestionAPIResponse = QuestionSuccessResponse | QuestionFailureResponse
