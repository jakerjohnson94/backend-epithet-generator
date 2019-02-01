import pytest
from helpers import Vocabulary, FileManager
import helpers.FileManager
import helpers.EpithetGenerator as ep

fm = FileManager()


def extension_test(self):
    path = "/foo/bar/file.json"
    assert fm.get_extension(path) == ".json"

