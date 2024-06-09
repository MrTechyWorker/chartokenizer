<p align="center">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/MrTechyWorker/chartokenizer/blob/main/docs/logo.png">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/MrTechyWorker/chartokenizer/blob/main/docs/logo.png">
    <img alt="Hashnode logo" src="https://github.com/MrTechyWorker/chartokenizer/blob/main/docs/logo.png" height="170">
    </picture>

</p>

<p align="center">
    <a href="https://"><img src="https://img.shields.io/badge/Python-%3E=_3.6-orange?logo=Python&logoColor=white" alt="Python - &gt;= 3.6"></a>
    <a href="#license"><img src="https://img.shields.io/badge/License-Apache-blue" alt="License"></a>
    <a href="https://pypi.org/project/chartokenizer"><img src="https://img.shields.io/badge/PyPi-chartokenizer-blueviolet?logo=Pypi&logoColor=white" alt="PyPi - chartokenizer"></a>


</p>

<h4 align="center">
    <p>
        <a href="/docs/usage.md">Documentation</a> |
        <a href="https://pypi.org/project/chartokenizer/">Pypi</a> |
        <a href="https://github.com/MrTechyWorker">Author</a> 
    <p>
</h4>

Chartokenizer is a Python package for basic character-level tokenization. It provides functionality to generate a character-to-index mapping for tokenizing strings at the character level. This can be useful in various natural language processing (NLP) tasks where text data needs to be preprocessed for analysis or modeling.

## Author: Shashank Kanna R

---
## 🚀 Benefits

1. Generates a character-to-index mapping for tokenizing strings.
  
  ```python
  text = "This is a Demo Text."
  
  # When tokenized using chartokenizer
  
  {' ': 0, '.': 1, 'D': 2, 'T': 3, 'a': 4, 'e': 5, 'h': 6, 'i': 7, 'm': 8, 'o': 9, 's': 10, 't': 11, 'x': 12}
  ```
2. Supports both custom character sets and a predefined classic character set.
   
  ```python
   # Predefined_classic_character_set
   
   r" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~"
  ```
- Provides tokenization and detokenization functions.
 ```bash
  # For predefined character set

  "hello" => tokenize => [68, 65, 72, 72, 75]

  [68, 65, 72, 72, 75] => detokenize => "hello"
 ```
- Allows saving and loading the character-to-index mapping dictionary to/from a file.
- Supports padding or truncating tokenized sequences to a fixed length.
```bash
# Padding "hello" to length of 10 with values of 0

"hello" => tokenize => [68, 65, 72, 72, 75] => pad_sequence => [68, 65, 72, 72, 75, 0, 0, 0, 0, 0]
```
---

## ⬇️ Installation

`chartokenizer` is available as a PyPi package<br>
<br>
<a href="https://pypi.org/project/chartokenizer/"><img src="https://img.shields.io/badge/PyPi-chartokenizer-2ea44f?style=for-the-badge&logo=PyPi&logoColor=white" alt="PyPi - chartokenizer"></a>

You can install via pip:

```bash
pip install chartokenizer
```
---
## ✅ Usage

[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](/docs/usage.md "Go to project documentation")

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

For more detailed usage and options, refer to the [documentation](/docs/usage.md)

---

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on [GitHub](https://github.com/MrTechyWorker/chartokenizer).

---

## License

Released under [Apache](/LICENSE) by [@MrTechyWorker](https://github.com/MrTechyWorker).

---

## Acknowledgments

- This package was inspired by the need for a simple and efficient character-level tokenizer in natural language processing tasks.
---
> Learn, Build, Develop !! 😉
---
