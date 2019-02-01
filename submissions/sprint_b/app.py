from sprint_b import app
from sprint_b.helpers import Vocabulary, FileManager
from sprint_b.helpers import EpithetGenerator as ep
import os
import json


path = "../../resources/data.json"


@app.route("/")
def epithets():
    epithets = ep.generate_epithets(path, 1)
    return json.dumps({"epithets": epithets})


@app.route("/vocabulary")
def vocabulary():
    cols = Vocabulary.from_file(path)
    return json.dumps({"vocabulary": cols})
