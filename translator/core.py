from dataclasses import dataclass
from typing import List, Generator

try:
    from googletrans import Translator as GoogleTranslator
except Exception:  # pragma: no cover - import may fail if library missing
    GoogleTranslator = None

class TranslationError(Exception):
    """Wyjątek zgłaszany w przypadku błędów tłumaczenia."""
    pass

@dataclass
class TranslationRecord:
    source_text: str
    dest_language: str
    translated_text: str

class TranslatorClient:
    """Owijka na googletrans.Translator wraz z historią tłumaczeń."""

    def __init__(self):
        if GoogleTranslator is None:
            raise TranslationError(
                "Biblioteka googletrans jest wymagana do wykonywania tłumaczeń"
            )
        self._translator = GoogleTranslator()
        self.history: List[TranslationRecord] = []

    def translate(self, text: str, dest_language: str) -> str:
        """Przetłumacz tekst i zapisz wynik w historii."""
        try:
            result = self._translator.translate(text, dest=dest_language)
            record = TranslationRecord(text, dest_language, result.text)
            self.history.append(record)
            return result.text
        except ValueError as val_err:
            raise TranslationError(f"Niepoprawne parametry: {val_err}") from val_err
        except Exception as exc:
            raise TranslationError(f"Nieoczekiwany błąd: {exc}") from exc

    def history_texts(self) -> Generator[str, None, None]:
        """Zwróć wszystkie przetłumaczone teksty z historii."""
        for record in self.history:
            yield record.translated_text

    def average_length(self) -> float:
        """Zwróć średnią długość przetłumaczonych tekstów z użyciem NumPy."""
        try:
            import numpy as np
        except ImportError as exc:
            raise TranslationError(
                "Do działania average_length wymagana jest biblioteka NumPy"
            ) from exc
        lengths = np.array([len(r.translated_text) for r in self.history])
        return float(np.mean(lengths)) if len(lengths) else 0.0
