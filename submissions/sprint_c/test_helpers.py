import pytest
from sprint_b.helpers import Vocabulary, FileManager, EpithetGenerator

voc = Vocabulary
ep = EpithetGenerator


csv_path = "../../resources/data.csv"
json_path = "../../resources/data.json"
test_path = "../../resources/test_data.json"

epithet = "artless base-court apple-john"


class TestFileManager(object):
    def test_json_ext(self):
        assert voc.files.get_extension(json_path) == "json"

    def test_csv_ext(self):
        assert voc.files.get_extension(csv_path) == "csv"

    def test_fail_ext(self):
        assert voc.files.get_extension(json_path) != "csv"

    def test_read_json(self):
        assert voc.files.read_json(json_path)


class TestVocabulary(object):
    def test_from_file(self):
        assert voc.from_file(json_path)

    def test_from_json(self):
        assert voc.from_json(json_path)

    def test_strategies(self):
        assert voc.strategies("json")


class TestEpithet(object):
    def test_select_words(self):
        assert type(ep.select_words(test_path)) is list

    def test_generate_epithets(self):
        ep_list = ep.generate_epithets(test_path, 1)[0].split(" ")
        assert ep_list
        assert len(ep_list) == 3
        assert epithet in " ".join(ep_list)

