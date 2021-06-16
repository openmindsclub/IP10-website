from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

from my_app import app
from my_app import models
from my_app.exceptions import *

api = Api(app)
CORS(app)

class home(Resource):
    def get(self):
        return redirect("http://localhost:8080/")
api.add_resource(home,'/')

class feedback(Resource):
    def post(self):
        insert = models.create_feedback(request.json["name"], request.json["email"], request.json["message"])
        if (insert):
            return jsonify({"Success":"Feedback added successfully"})
        else:
            return jsonify({"Error": "Can't add feedback"})
api.add_resource(feedback, '/feedback')

class participant(Resource):
    def post(self):
        try:
            inserted = models.create_participant(request.json['first_name'], request.json['last_name'], request.json['email'], request.json['date_of_birth'], request.json['conferences'], request.json['activites'], request.json['chasse_au_tresor'], request.json['isUSTHB'], request.json['Whichuniversity'])
        except EmailAlreadyExistError as e:
            return jsonify({"error": "The email is already being used"})

        if (inserted):
            return jsonify({"success":"Paritcipant added successfully"})
        else:
            return jsonify({"error": "Can't add participant"})
api.add_resource(participant,'/register')


if __name__ == "__main__":
    app.run()
