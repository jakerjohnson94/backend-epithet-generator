import os
import json
import csv
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

    @staticmethod
    def read_csv(path, mode="r"):
        """reads data from a csv file path"""
        data = {"Column 1": [], "Column 2": [], "Column 3": []}
        with open(path, newline="") as csvfile:
            payload = csv.reader(csvfile)
            data_list = list(payload)[1:]
            for c1, c2, c3 in data_list:
                if c1 is not "":
                    data["Column 1"].append(c1)
                if c2 is not "":
                    data["Column 2"].append(c2)
                if c3 is not "":
                    data["Column 3"].append(c3)
            return data


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path):
        """decides how to represent data based on fyle type"""
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path)
        return representation

    @classmethod
    def from_json(cls, path):
        """reads data from a json file path"""
        data = cls.files.read_json(path)
        return data

    @classmethod
    def from_csv(cls, path):
        """reads data from a json file path"""
        data = cls.files.read_csv(path)
        return data

    @classmethod
    def strategies(cls, file_extension, intent="read"):
        """calls appropriate file handling method based on what user wants to do with file"""
        input_strategies = {"json": cls.from_json, "csv": cls.from_csv}
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

