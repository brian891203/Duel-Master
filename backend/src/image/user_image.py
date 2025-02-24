# standard library
from base64 import b64encode
import json
import os
import requests

# 3rd party library
from werkzeug.datastructures import FileStorage

# local module
from ..constants import API, PATH
from src.utils.misc import try_getenv


class UserImage:
    def __init__(self, image: FileStorage) -> None:
        """使用者上傳圖片

        Parameters
        ----------
        image : FileStorage
            使用者上傳圖片
        """
        self._image = image
        self.filename = image.filename

    @property
    def abspath(self) -> str:
        """使用者上傳圖片在本地的絕對路徑"""
        return f"{PATH.USER_UPLOAD_IMAGE_DIR.value}/{self.filename}"

    def save(self) -> None:
        """將使用者上傳圖片儲存至本地"""
        self._image.save(self.abspath)

    def remove(self) -> None:
        """將使用者上傳圖片自本地移除"""
        if os.path.exists(self.abspath):
            os.remove(self.abspath)

    def create_url(self) -> str:
        """將使用者上傳圖片再上傳到 Imgur，回傳其 URL

        Returns
        -------
        str
            URL
        """

        api_key = try_getenv("IMGUR_API_KEY")
        client_id = try_getenv("IMGUR_CLIENT_ID")

        response = requests.post(
            API.IMGUR.value,
            headers={"Authorization": f"Client-ID {client_id}"},
            data={
                "key": api_key,
                "image": b64encode(open(self.abspath, "rb").read()),
                "type": "base64",
                "name": self.filename,
                "title": self.filename,
            },
        )

        url = json.loads(response.text)["data"]["link"]

        return url
