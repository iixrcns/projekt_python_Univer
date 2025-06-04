import argparse
from translator import TranslatorClient, TranslationError


def interactive_loop(client: TranslatorClient) -> None:
    """Uruchom interaktywną sesję tłumaczenia."""
    while True:
        try:
            text = input(
                "Wpisz tekst do przetłumaczenia (pozostaw puste, aby zakończyć): "
            ).strip()
        except EOFError:
            break
        if not text:
            break
        dest = input("Kod języka docelowego: ").strip()
        try:
            translation = client.translate(text, dest)
            print(translation)
        except TranslationError as exc:
            print(f"Tłumaczenie nie powiodło się: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tłumacz teksty za pomocą Google Translate")
    parser.add_argument("text", nargs="?", help="Tekst do przetłumaczenia")
    parser.add_argument(
        "dest",
        nargs="?",
        help="Kod języka docelowego, np. en, fr, de",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Uruchom tryb interaktywny",
    )
    args = parser.parse_args()

    client = TranslatorClient()

    if args.interactive:
        interactive_loop(client)
        return

    if args.text is None or args.dest is None:
        parser.error("wymagane argumenty: text dest")

    try:
        translation = client.translate(args.text, args.dest)
        print(translation)
    except TranslationError as exc:
        print(f"Tłumaczenie nie powiodło się: {exc}")


if __name__ == "__main__":
    main()
