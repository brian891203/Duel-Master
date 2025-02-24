# standard library
import os
import logging

# 3rd party library
import requests

# local module
from src.constants import API, PATH


class CardImage:
    def __init__(self, card_id: str, *, logger: logging.Logger) -> None:
        """卡面圖片

        Parameters
        ----------
        card_id : str
            卡片的 ID
        logger : logging.Logger
            日誌 logger
        """
        self.card_id = card_id
        self.image_url = f"{API.YUGIOH_IMAGE.value}/{self.card_id}.jpg"
        self.local_path = f"{PATH.YUGIOH_IMAGE_DIR.value}/{self.card_id}.jpg"
        self.logger = logger

    def exists_locally(self) -> bool:
        """檢查卡面圖片是否已存在本地"""
        return os.path.exists(self.local_path)

    def download(self) -> bool:
        """下載卡面圖片並儲存至本地"""
        try:
            response = requests.get(self.image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.error(
                f"Error downloading image {self.card_id}. Error Message - {e}"
            )
            return False
        else:
            with open(self.local_path, "wb") as file:
                file.write(response.content)
            self.logger.debug(f"Image {self.card_id} downloaded successfully.")
            return True

    def remove(self) -> None:
        """移除本地儲存的圖片"""
        if self.exists_locally():
            os.remove(self.local_path)
            self.logger.debug(f"Image {self.card_id} removed from local storage.")
        else:
            self.logger.warning(
                f"Attempted to remove {self.card_id}, but file does not exist."
            )
