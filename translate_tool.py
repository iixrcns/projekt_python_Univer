import argparse
from translator import TranslatorClient, TranslationError


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate text using Google Translate")
    parser.add_argument("text", help="Text to translate")
    parser.add_argument(
        "dest", help="Destination language code, e.g. en, fr, de")
    args = parser.parse_args()

    client = TranslatorClient()
    try:
        translation = client.translate(args.text, args.dest)
        print(translation)
    except TranslationError as exc:
        print(f"Translation failed: {exc}")


if __name__ == "__main__":
    main()
