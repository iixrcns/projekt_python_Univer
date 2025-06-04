import unittest
from unittest.mock import patch, MagicMock

from translator.core import TranslatorClient, TranslationError


class DummyResult:
    def __init__(self, text):
        self.text = text


class TranslatorClientTest(unittest.TestCase):
    @patch('translator.core.GoogleTranslator')
    def test_translate_success(self, mock_translator_cls):
        mock_instance = mock_translator_cls.return_value
        mock_instance.translate.return_value = DummyResult('Bonjour')

        client = TranslatorClient()
        result = client.translate('Hello', 'fr')
        self.assertEqual(result, 'Bonjour')
        self.assertEqual(len(client.history), 1)
        self.assertEqual(client.history[0].translated_text, 'Bonjour')

    @patch('translator.core.GoogleTranslator')
    def test_translate_error(self, mock_translator_cls):
        mock_instance = mock_translator_cls.return_value
        mock_instance.translate.side_effect = ValueError('bad language')

        client = TranslatorClient()
        with self.assertRaises(TranslationError):
            client.translate('Hello', '??')


if __name__ == '__main__':
    unittest.main()
