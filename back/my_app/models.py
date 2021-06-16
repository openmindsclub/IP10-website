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


def create_participant(first_name, last_name, email, birth_day, list_conferences, activities, chasse_au_tresor, is_usthb, which_univ):

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
        "birth_day": birth_day,
        "email": email,
        "conferences" : list_conferences,
        "activites": activities,
        "chasse_au_tresor": chasse_au_tresor,
        "is_usthb": is_usthb,

    }

    if not is_usthb:
        post["which_univ"] = which_univ

    return participant_col.insert_one(post)
