# chartokenizer/tokenizer.py

import json

class Tokenizer:
    def initialize(self, string: str = "", classic: bool = False, case_sensitive: bool = True) -> dict:
        
        """
        Initializes a character-to-index mapping for a basic character-level tokenizer.

        - Generates a unique set of characters from the provided text and maps each character to a unique index.
        - If no string is provided, returns an empty dictionary.
        - If the "classic" parameter is set to True, uses a predefined set of characters.
        - The predefined (classic) character set includes:
          !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~
        - The "case_sensitive" parameter determines if the character set should distinguish between upper and lower case.

        Args:
            string (str, optional): The input text to derive the character set from. Defaults to an empty string.
            classic (bool, optional): Flag to use the predefined classic character set. Defaults to False.
            case_sensitive (bool, optional): Flag to handle case sensitivity. Defaults to True.

        Returns:
            dict: A dictionary mapping each character to a unique index.
        """

        if string != "" and classic == True:
            raise AttributeError("Non empty String and and classic = True cannot be simultaniously passed")
        if classic:
            char_set = r" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~"
        else:
            if not case_sensitive:
                string = string.lower()
            char_set = "".join(sorted(set(string)))
        
        d = {char: i for i, char in enumerate(char_set)}
        return d

    def tokenize(self, dictionary: dict, string: str, handle_unknown: str = "error") -> list:
        """
        Tokenizes the given string using the provided character-to-index mapping.

        Converts each character in the input string to its corresponding index based on the provided dictionary.

        Args:
            dictionary (dict): The character-to-index mapping dictionary.
            string (str): The input string to tokenize. Defaults to an empty string.
            handle_unknown (str, optional): Specifies how to handle unknown characters ("error", "ignore", or "replace"). Defaults to "error".

        Returns:
            list: A list of tokenized values corresponding to the characters in the input string.

        Raises:
            KeyError: If the input string contains characters not present in the dictionary and handle_unknown is set to "error".
        """
        if handle_unknown not in {"error", "ignore", "replace"}:
            raise ValueError("handle_unknown must be 'error', 'ignore', or 'replace'.")

        tokens = []
        for char in string:
            if char in dictionary:
                tokens.append(dictionary[char])
            else:
                if handle_unknown == "error":
                    raise KeyError(f"The input string contains an unspecified character '{char}'.")
                elif handle_unknown == "replace":
                    tokens.append(dictionary.get("<UNK>", -1))  # Assuming <UNK> is used for unknowns, else -1
        return tokens

    def detokenize(self, dictionary: dict, tokens: list) -> str:
        """
        Converts a list of tokenized values back into the original string.

        Args:
            dictionary (dict): The character-to-index mapping dictionary.
            tokens (list): The list of tokenized values.

        Returns:
            str: The original string reconstructed from the tokens.

        Raises:
            KeyError: If a token is not present in the dictionary.
        """
        reverse_dictionary = {i: char for char, i in dictionary.items()}
        try:
            return "".join(reverse_dictionary[token] for token in tokens)
        except KeyError as e:
            raise KeyError(f"The token '{e.args[0]}' is not present in the dictionary.")

    def save_dictionary(self, dictionary: dict, filepath: str):
        """
        Saves the character-to-index mapping dictionary to a file.

        Args:
            filepath (str): The file path where the dictionary will be saved.
        """
        with open(filepath, 'w') as file:
            json.dump(dictionary, file)

    def load_dictionary(self, filepath: str):
        """
        Loads the character-to-index mapping dictionary from a file.

        Args:
            filepath (str): The file path from which the dictionary will be loaded.
        
        Returns:
            dictionary: The loaded data from the file
        """
        with open(filepath, 'r') as file:
            d = json.load(file)
        return {char: i for char, i in d.items()}

    def pad_sequence(self, tokens: list, max_length: int, padding_value: int = 0) -> list:
        """
        Pads or truncates the tokenized sequence to a fixed length.

        Args:
            tokens (list): The list of tokenized values.
            max_length (int): The desired sequence length.
            padding_value (int, optional): The value to use for padding. Defaults to 0.

        Returns:
            list: The padded or truncated sequence.
        """

        if len(tokens) < max_length:
            tokens.extend([padding_value] * (max_length - len(tokens)))
        return tokens[:max_length]
