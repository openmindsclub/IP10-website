from flask import Flask
from pymongo import database
from flask_pymongo import PyMongo

app = Flask(__name__)
#mongo configuration
#database name
db_name = "omcIP"
############################################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/"+db_name
mongo = PyMongo(app)
#############################################################
#feedback collection
feedbacks_col = mongo.db['feedbacks']

#participant collection
participant_col = mongo.db['participant']
#verifing email
def email_exist(email):
    result = participant_col.find_one({"email":email})
    return result != None
#add feedback
def create_feedback(name, email, message):
    post = {
        "name":name,
        "email":email,
        "message":message
    }
    feedbacks_col.insert_one(post)
#Add participant
def create_participant(first_name, last_name, email, status,date_of_birth, conferences,workshops, chasse_au_tresor = False, battle_grap = False):
    if email_exist(email):
        raise ValueError("the email already exist in the database")
    post = {
        "first_name":first_name,
        "last_name":last_name,
        "date_of_birth":date_of_birth,
        "email":email,
        "status": status,
        "conferences" : {
            "panel 1": conferences.panel1,
            "panel 2":conferences.panel1,
            "conference 1": conferences.conf1,
            "conference 2": conferences.conf2,
            "conference 3": conferences.conf3
        },
        "workshops": {
        "python":workshops.python,
        "godot": workshops.godot
        },
        "chasse au tresor": chasse_au_tresor,
        "battle graphique":battle_grap
        }
    participant_col.insert_one(post)
