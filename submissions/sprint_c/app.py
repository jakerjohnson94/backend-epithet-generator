from sprint_c import app
from sprint_c.helpers import Vocabulary, FileManager
from sprint_c.helpers import EpithetGenerator as ep
from flask import request
from random import randint
import os
import json


path = "../../resources/data.json"


@app.route("/")
@app.route("/epithets/<int:count>")
def epithets(count=1):
    epithets = ep.generate_epithets(path, count)
    return json.dumps({"epithets": epithets})


@app.route("/epithets/random")
def random_epithets():
    count = randint(1, 100)
    return epithets(count)


@app.route("/vocabulary")
def vocabulary():
    cols = Vocabulary.from_file(path)
    return json.dumps({"vocabulary": cols})

