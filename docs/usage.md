
# Usage Guide for Chartokenizer

Chartokenizer is a Python package for basic character-level tokenization. This guide will walk you through the usage of the package, including how to generate a character-to-index mapping, tokenize and detokenize strings, and save/load the mapping dictionary to/from a file.

## Table of Contents

- [Installation](#installation)
- [Initialization](#initialization)
- [Tokenization](#tokenization)
- [Detokenization](#detokenization)
- [Saving and Loading Dictionary](#saving-and-loading-dictionary)

## Installation

You can install `chartokenizer` via pip:

```bash
pip install chartokenizer
```

## Initialization

To initialize the tokenizer and generate the character-to-index mapping dictionary, follow these steps:

```python
from chartokenizer import Tokenizer

# Initialize the tokenizer
tokenizer = Tokenizer()

# Generate character-to-index mapping dictionary
# You can pass a string to derive characters from it or use the predefined classic character set
dictionary = tokenizer.initialize(string="your_text_here", classic=False, case_sensitive=True)
```

Parameters for `initialize` method:
- `string` (optional): The input text to derive the character set from. Defaults to an empty string.
- `classic` (optional): Flag to use the predefined classic character set. Defaults to False.
- `case_sensitive` (optional): Flag to handle case sensitivity. Defaults to True.
- `classic = True` Should be passed without the string parameter.
## Tokenization

Once you have the character-to-index mapping dictionary, you can tokenize a string using the `tokenize` method:

```python
# Tokenize a string
tokens = tokenizer.tokenize(dictionary, "your_text_here", handle_unknown="error")
```

Parameters for `tokenize` method:
- `dictionary`: The character-to-index mapping dictionary.
- `string` (optional): The input string to tokenize. Defaults to an empty string.
- `handle_unknown` (optional): Specifies how to handle unknown characters ("error", "ignore", or "replace"). Defaults to "error".

## Detokenization

To convert tokenized values back into the original string, you can use the `detokenize` method:

```python
# Detokenize tokens back to string
text = tokenizer.detokenize(dictionary, tokens)
```

Parameters for `detokenize` method:
- `dictionary`: The character-to-index mapping dictionary.
- `tokens`: The list of tokenized values.

## Saving and Loading Dictionary

You can save the character-to-index mapping dictionary to a file and load it later for reuse:

```python
# Save the dictionary to a file
tokenizer.save_dictionary(dictionary, "dictionary.json")

# Load the dictionary from a file
loaded_dictionary = tokenizer.load_dictionary("dictionary.json")
```

## Conclusion

This guide covered the basic usage of the Chartokenizer package, including initialization, tokenization, detokenization, and saving/loading the dictionary. For more advanced usage and options, refer to the package documentation or explore additional features provided by the package.

---