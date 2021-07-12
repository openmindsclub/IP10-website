from flask import Flask
from pymongo import database
from flask_pymongo import PyMongo

from my_app import app
from my_app.exceptions import *

# mongo configuration
db_name = "omcIP" # database name
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + db_name
mongo = PyMongo(app)
graphic_battle_col = mongo.db["graphic_battle"]
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

def create_graphic_battle(email, link):
    """
    insert a feedback into the database

    Parameters:
         email(str), link(str)
    """

    post = {
        "email": email,
        "link": link,
    }
    return graphic_battle_col.insert_one(post)


def create_participant(first_name, last_name, email, list_conferences, workshops, chasse_au_tresor, battle_graphique, is_usthb, which_univ):

    """
    function that's insert a participant to the database

    Parameters:
        first_name and last_name(str)
        email(str): will be stocked in the data base, it's unique so we check if it
                exist and raise an ValueError exception if it does
        date_of_birth(str): date of birth

        phone_number(str)
        conferences(dict of bools): dict of booleans which contains all 5
                conferences and panels, true if he registered to one of them,
                and false elswhere
        activities(str): which activity the participant want to participate between
                the 2 workshops, and the battle graphic,
                can take the values "python", "godot", "battle_graphique" or "" otherwise would raise an exeption
        chasse_au_tresor(bool): true if it participate in the tresor hunt, false if it doesn't
        is_usthb(bool): true if the participant is from USTHB
        which_univ(str): wich university the participant belong to (if it's not USTHB)
                    if is_usthb is true the value of which_univ is ignored

    Raises:
        EmailAlreadyExistError if the email already exist in the database.
        InvalidActivityError if the email already exist in the database.

    Return:
        True if the particiapant was added successfully and false elswhere
    """

    _data_verification(email, list_conferences, workshops, chasse_au_tresor, is_usthb, which_univ)

    list_conferences = [conf.lower() for conf in list_conferences]

    post = {
        "first_name": first_name.lower(),
        "last_name": last_name.lower(),
        "email": email.lower(),
        "conferences" : list_conferences,
        "workshops": workshops.lower(),
        "battle_graphique": battle_graphique,
        "chasse_au_tresor": chasse_au_tresor,
        "is_usthb": is_usthb,
    }

    if not is_usthb:
        post["which_univ"] = which_univ.lower()

    return participant_col.insert_one(post)


def _data_verification(email, list_conferences, workshops, chasse_au_tresor, is_usthb, which_univ):

    if email_exist(email):
        raise EmailAlreadyExistError(email)

    if workshops.lower() not in ["", "python", "godot"]:
        raise InvalidActivityError(workshops)
