from dataclasses import dataclass
from typing import List, Generator

try:
    from googletrans import Translator as GoogleTranslator
except Exception:  # pragma: no cover - import may fail if library missing
    GoogleTranslator = None

class TranslationError(Exception):
    """Custom exception for translation errors."""
    pass

@dataclass
class TranslationRecord:
    source_text: str
    dest_language: str
    translated_text: str

class TranslatorClient:
    """Wraps googletrans.Translator and keeps history of translations."""

    def __init__(self):
        if GoogleTranslator is None:
            raise TranslationError(
                "googletrans library is required to perform translations")
        self._translator = GoogleTranslator()
        self.history: List[TranslationRecord] = []

    def translate(self, text: str, dest_language: str) -> str:
        """Translate text and store the result in history."""
        try:
            result = self._translator.translate(text, dest=dest_language)
            record = TranslationRecord(text, dest_language, result.text)
            self.history.append(record)
            return result.text
        except ValueError as val_err:
            raise TranslationError(f"Invalid parameters: {val_err}") from val_err
        except Exception as exc:
            raise TranslationError(f"Unexpected error: {exc}") from exc

    def history_texts(self) -> Generator[str, None, None]:
        """Yield all translated texts from history."""
        for record in self.history:
            yield record.translated_text

    def average_length(self) -> float:
        """Return the average length of translated texts using NumPy."""
        try:
            import numpy as np
        except ImportError as exc:
            raise TranslationError("NumPy is required for average_length") from exc
        lengths = np.array([len(r.translated_text) for r in self.history])
        return float(np.mean(lengths)) if len(lengths) else 0.0
