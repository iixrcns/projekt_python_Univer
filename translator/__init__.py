"""Pakiet narzędzi do tłumaczeń."""

from .core import TranslatorClient, TranslationError, TranslationRecord

__all__ = [
    "TranslatorClient",
    "TranslationError",
    "TranslationRecord",
]
