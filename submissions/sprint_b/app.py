from sprint_b import app
from sprint_b.helpers import Vocabulary, FileManager
from sprint_b.helpers import EpithetGenerator as ep
from flask import request
import os
import json


path = "../../resources/data.json"


@app.route("/")
@app.route("/epithets/<int:count>")
def epithets(count=1):
    epithets = ep.generate_epithets(path, count)
    return json.dumps({"epithets": epithets})


@app.route("/vocabulary")
def vocabulary():
    cols = Vocabulary.from_file(path)
    return json.dumps({"vocabulary": cols})

