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
    result = participant_col.find_one({"email": email})
    return result != None


def create_feedback(name, email, message):
    """
    insert a feedback into the database

    Parameters:
        name(str), email(str), message(str)
    """

    post = {
        "name": name,
        "email": email,
        "message": message
    }
    return feedbacks_col.insert_one(post)


def create_participant(first_name, last_name, email, status, date_of_birth, conferences, workshops, chasse_au_tresor=False, battle_grap=False, team_emails=[]):

    """
    function that's insert a participant to the database

    Parameters:
        first_name and last_name(str)
        email(str): will be stocked in the data base, it's unique so we check if it
                exist and raise an ValueError exception if it does
        date_of_birth(str): date of birth
        gender(str): "male", "female" or "other"
        status(str): one of the following strings "Unemployed", "High schooler",
                "Undergraduate", "Graduate", "Masters", "Doctorate", "Employed", "Freelance", "Other"
        phone_number(str)
        conferences(dict of bools): dict of booleans which contains all 5
                conferences and panels, true if he registered to one of them,
                and false elswhere
        workshops(dict of bools): dict of booleans which contains the 2 disponible
                workshops, true if he registered to one of them, and false elswhere
        chasse_au_tresor(bool): true if it participate in the tresor hunt, false if it doesn't, Default:False
        battle_grap(bool): true if it participate in the battle graphique, false if it doesn't, Default:False
        team_emails(list of str): contains the lists of the teams members in the tresor hunt
                    is only taken into consideration if chasse_au_tresor=True, Default:[]

    Raises:
        EmailAlreadyExistError if the email already exist in the database.

    Return:
        True if the particiapant was added successfully and false elswhere
    """


    if email_exist(email):
        raise EmailAlreadyExistError(email)

    post = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "email": email,
        "status": status,
        "conferences" : {
            "panel1": conferences["panel1"],
            "panel2": conferences["panel2"],
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

    if chasse_au_tresor:
        post["team_emails"] = team_emails

    return participant_col.insert_one(post)
