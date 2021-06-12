from flask import Flask
from pymongo import database
from flask_pymongo import PyMongo

from my_app import app
from my_app.exceptions import *

# mongo configuration
db_name = "omcIP" # database name
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + db_name
mongo = PyMongo(app)
feedbacks_col = mongo.db['feedbacks'] # participant collection
participant_col = mongo.db['participant'] # verifing email

def email_exist(email):
    result = participant_col.find_one({"email":email})
    return result != None


def create_feedback(name, email, message):
    post = {
        "name":name,
        "email":email,
        "message":message
    }
    return feedbacks_col.insert_one(post)


def create_participant(first_name, last_name, email, status, date_of_birth, conferences, workshops, chasse_au_tresor = False, battle_grap = False):
    if email_exist(email):
        raise EmailAlreadyExistError(email)
    post = {
        "first_name":first_name,
        "last_name":last_name,
        "date_of_birth":date_of_birth,
        "email":email,
        "status": status,
        "conferences" : {
            "panel1": conferences["panel1"],
            "panel2":conferences["panel2"],
            "conference1": conferences["conference1"],
            "conference2": conferences["conference2"],
            "conference3": conferences["conference3"]
        },
        "workshops": {
        "python":workshops["python"],
        "godot": workshops["godot"]
        },
        "chasse_au_tresor": chasse_au_tresor,
        "battle_graphique":battle_grap
        }
    return participant_col.insert_one(post)
