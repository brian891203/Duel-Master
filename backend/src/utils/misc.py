# standard library
import os


def try_getenv(key: str) -> str:
    """
    獲取環境變數，若不存在則拋出 ValueError
    """

    env = os.getenv(key)
    if env is None:
        raise ValueError(f"{key} environment variable is not set")

    return env