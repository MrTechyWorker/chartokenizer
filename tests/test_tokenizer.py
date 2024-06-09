# tests/test_tokenizer.py

import unittest
from chartokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_initialize_classic(self):
        dictionary = self.tokenizer.initialize(classic=True)
        self.assertEqual(dictionary['A'], 32)  # Corrected index
        self.assertEqual(dictionary['a'], 61)

    def test_initialize_custom_string(self):
        dictionary = self.tokenizer.initialize(string="hello")
        self.assertEqual(dictionary['h'], 1)  # 'e' comes before 'h' in sorted set
        self.assertEqual(dictionary['e'], 0)  # 'e' comes before 'h' in sorted set
        self.assertEqual(dictionary['l'], 2)
        self.assertEqual(dictionary['o'], 3)

    def test_tokenize(self):
        dictionary = self.tokenizer.initialize(string="hello")
        tokens = self.tokenizer.tokenize(dictionary, "hello")
        self.assertEqual(tokens, [1, 0, 2, 2, 3])

    def test_tokenize_with_unknown(self):
        dictionary = self.tokenizer.initialize(string="hello")
        with self.assertRaises(KeyError):
            self.tokenizer.tokenize(dictionary, "world")

    def test_detokenize(self):
        dictionary = self.tokenizer.initialize(string="hello")
        tokens = [1, 0, 2, 2, 3]
        text = self.tokenizer.detokenize(dictionary, tokens)
        self.assertEqual(text, "hello")

    def test_pad_sequence(self):
        tokens = [1, 2, 3]
        padded = self.tokenizer.pad_sequence(tokens, 5)
        self.assertEqual(padded, [1, 2, 3, 0, 0])

    def test_save_and_load_dictionary(self):
        dictionary = self.tokenizer.initialize(string="hello")
        self.tokenizer.save_dictionary(dictionary, "test_dict.json")
        loaded_dictionary = self.tokenizer.load_dictionary("test_dict.json")
        self.assertEqual(dictionary, loaded_dictionary)

if __name__ == "__main__":
    unittest.main()
