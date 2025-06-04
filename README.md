# projekt_python_Univer
Project Python 1 cyckle

## Translation Tool

This repository contains a small translation utility organized as a Python
package. The main entry point is `translate_tool.py` which relies on the
`translator` package. Translations are performed using the Google Translate API
via the `googletrans` library. The package also demonstrates the use of Python
`dataclasses`, generators, and even integrates a small function that utilises
NumPy.

### Usage

```bash
python translate_tool.py "Hello" fr
```

### Interactive Mode

Run the tool with `-i` to translate multiple phrases sequentially. Leave the
text input blank to exit:

```bash
python translate_tool.py -i
```

Make sure `googletrans` and `numpy` are installed in your environment. The tool
prints the translated text or an error message when something goes wrong.
