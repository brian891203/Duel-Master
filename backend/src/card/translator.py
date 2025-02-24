# standard library
from abc import ABC, abstractmethod
import logging

# 3rd party library
import torch
from transformers import MT5ForConditionalGeneration, AutoTokenizer

# local module
from src.constants import PATH


class AbstractTranslator(ABC):
    @abstractmethod
    def translate(self, untranslated_text: str) -> str:
        pass


class YugiohTranslator(AbstractTranslator):
    def __init__(self, *, logger: logging.Logger):
        self.logger = logger
        self.model_path = PATH.MODEL_DIR.value
        self.model_revision = "defualt_0321-0402"

        # device
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.logger.debug("[YugiohTranslator] - using device: %s", self._device)

        # tokenizer
        self.logger.debug("[YugiohTranslator] - loading tokenizer...")
        self._tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, trust_remote_code=True
        )
        self.logger.debug("[YugiohTranslator] - tokenizer ready")

        # model
        self.logger.debug("[YugiohTranslator] - loading model...")
        self._model = MT5ForConditionalGeneration.from_pretrained(
            self.model_path, revision=self.model_revision
        ).to(self._device)
        self.logger.debug("[YugiohTranslator] - model ready")

    def translate(self, untranslated_text: str) -> str:
        self.logger.debug("[YugiohTranslator] - translation started")

        top_k: int = 50
        max_length: int = 768
        top_p: float = 0.95
        temperature: float = 0.1
        num_return_sequences: int = 1
        prefix = "<-ja2zh->"

        encodings_text = self._tokenizer.encode(
            prefix + untranslated_text,
            return_tensors="pt",
            max_length=max_length,
            padding="max_length",
            truncation=True,
        ).to(self._device)

        output = self._model.generate(
            encodings_text,
            do_sample=True,
            top_k=top_k,
            max_length=max_length,
            top_p=top_p,
            temperature=temperature,
            num_return_sequences=num_return_sequences,
        )

        translated_text = [
            self._tokenizer.decode(o, skip_special_tokens=True) for o in output
        ][0]

        self.logger.debug(
            "[YugiohTranslator] - translation completed.\nResult:\n%s", translated_text
        )

        return translated_text
