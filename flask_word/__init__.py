from flask import Flask
import json

"For Secret_Key"
from flask_word.config import Config



"like we marked this script, create app variable"
app = Flask(__name__)

"we pass this object as configuration"
app.config.from_object(Config)


"errors handling"
from flask_word.errors.handlers import errors
app.register_blueprint(errors)

with open(r"words_dictionary.json") as d:
    word_list = json.load(d)


"also to avoid circular import put this at the end"
from flask_word import routes
