
# Chartokenizer

Chartokenizer is a Python package for basic character-level tokenization. It provides functionality to generate a character-to-index mapping for tokenizing strings at the character level. This can be useful in various natural language processing (NLP) tasks where text data needs to be preprocessed for analysis or modeling.

## 🚀 Benifits

- Generates a character-to-index mapping for tokenizing strings.
- Supports both custom character sets and a predefined classic character set.
- Provides tokenization and detokenization functions.
- Allows saving and loading the character-to-index mapping dictionary to/from a file.
- Supports padding or truncating tokenized sequences to a fixed length.

## ⬇️ Installation

You can install `chartokenizer` via pip:

```bash
pip install chartokenizer
```

## ✅ Usage

```python
from chartokenizer import Tokenizer

# Initialize the tokenizer
tokenizer = Tokenizer()

# Generate character-to-index mapping dictionary
dictionary = tokenizer.initialize(string="your_text_here")

# Tokenize a string
tokens = tokenizer.tokenize(dictionary, "your_text_here")

# Detokenize tokens back to string
text = tokenizer.detokenize(dictionary, tokens)
```

For more detailed usage and options, refer to the [documentation](https://github.com/your_username/chartokenizer/blob/main/docs/usage.md).

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on [GitHub](https://github.com/MrTechyWorker/chartokenizer).

## License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/MrTechyWorker/chartokenizer/LICENSE) file for details.

## Acknowledgments

- This package was inspired by the need for a simple and efficient character-level tokenizer in natural language processing tasks.

> Learn, Build, Develop !! 😉
---
