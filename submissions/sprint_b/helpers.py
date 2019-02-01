import os
import json
import random


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode="r"):
        """reads data from a json file path"""
        with open(path, mode=mode) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """decides how to represent data based on fyle type"""
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, *args, **kwargs):
        """reads data from a json file path"""
        data = cls.files.read_json(path, *args, **kwargs)
        return data

    @classmethod
    def strategies(cls, file_extension, intent="read"):
        """calls appropriate file handling method based on what user wants to do with file"""
        input_strategies = {"json": cls.from_json}
        if intent is "read":
            return input_strategies[file_extension]


class EpithetGenerator:
    """Generates an epithet that randomnly selects one word from each a Vocabulary file"""

    vocabulary = Vocabulary()

    @classmethod
    def select_words(cls, path):
        """Selects a random word from one of each data column and appends them to an array"""
        vocab = cls.vocabulary.from_file(path)
        cols = [vocab["Column 1"], vocab["Column 2"], vocab["Column 3"]]
        words = []
        for col in cols:
            random_index = random.randint(0, len(col) - 1)
            words.append(col[random_index])
        return words

    @classmethod
    def generate_epithets(cls, path, count):
        """generates a number of epithet strings from selected words"""
        epithets = []
        for _ in range(count):
            epithet = " ".join(cls.select_words(path))
            epithets.append(epithet)
        return epithets

