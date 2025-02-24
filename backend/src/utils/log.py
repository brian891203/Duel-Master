# standard library
import logging


def getDummyLogger() -> logging.Logger:
    dummy_logger = logging.getLogger("dummy")
    dummy_logger.addHandler(logging.NullHandler())
    return dummy_logger
