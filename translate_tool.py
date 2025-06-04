import argparse
from translator import TranslatorClient, TranslationError


def interactive_loop(client: TranslatorClient) -> None:
    """Run an interactive translation session."""
    while True:
        try:
            text = input("Enter text to translate (leave blank to quit): ").strip()
        except EOFError:
            break
        if not text:
            break
        dest = input("Destination language code: ").strip()
        try:
            translation = client.translate(text, dest)
            print(translation)
        except TranslationError as exc:
            print(f"Translation failed: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Translate text using Google Translate")
    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument(
        "dest", nargs="?", help="Destination language code, e.g. en, fr, de")
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Run interactive mode")
    args = parser.parse_args()

    client = TranslatorClient()

    if args.interactive:
        interactive_loop(client)
        return

    if args.text is None or args.dest is None:
        parser.error("the following arguments are required: text dest")

    try:
        translation = client.translate(args.text, args.dest)
        print(translation)
    except TranslationError as exc:
        print(f"Translation failed: {exc}")


if __name__ == "__main__":
    main()
