from flask import Flask, json, request, jsonify
from pymongo import database
from werkzeug.utils import redirect
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from flask_cors import CORS
########################################################################################################################################

app = Flask(__name__)
api = Api(app)
CORS(app)
#mongo configuration
db_name = "omcIP"
app.config["MONGO_URI"] = "mongodb://localhost:27017/"+db_name
mongo = PyMongo(app)
feedbacks_col = mongo.db['feedbacks']
participant_col = mongo.db['participant']

#functions
########################################################################################################################################
def email_exist(email):
    result = participant_col.find_one({"email":email})
    return result != None
########################################################################################################################################
def create_feedback(name, email, message):
    post = {
        "name":name,
        "email":email,
        "message":message
    }
    return feedbacks_col.insert_one(post)

########################################################################################################################################
#This is for creating a participant
########################################################################################################################################

def create_participant(first_name, last_name, email, status,date_of_birth, conferences,workshops, chasse_au_tresor = False, battle_grap = False):
    if email_exist(email):
        raise ValueError("the email already exist in the database")
    print(first_name, last_name, email, status,date_of_birth, conferences,workshops, chasse_au_tresor, battle_grap)
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
########################################################################################################################################
#api
#Home
class home(Resource):
    def get(self):
        return redirect("http://localhost:8080/")
api.add_resource(home,'/')
########################################################################################################################################
#Add Feedback
class feedback(Resource):
    def post(self):
        insert = create_feedback(request.json["name"], request.json["email"], request.json["message"])
        if (insert):
            return jsonify({"Success":"Feedback added successfully"})
        else:
            return jsonify({"Error": "Can't add feedback"})
api.add_resource(feedback, '/feedback/')
########################################################################################################################################
#Add participant
class participant(Resource):
    def post(self):
        inserted = create_participant(request.json['first_name'], request.json['last_name'], request.json['email'], request.json['status'], request.json['date_of_birth'], dict(request.json['conferences']), dict(request.json['workshops']), request.json['chasse_au_tresor'], request.json['battle_graphique'])
        if (inserted):
            return jsonify({"success":"Paritcipant added successfully"})
        else:
            return jsonify({"error": "Can't add participant"})
api.add_resource(participant,'/register/')
########################################################################################################################################

#debug
if __name__ == "__main__":
    app.run(debug=True)