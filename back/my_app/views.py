from flask import Flask, json, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

from my_app import app
from my_app import models
from my_app.exceptions import *

api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

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
        print(request.json)
        try:
            inserted = models.create_participant(request.json['first_name'], request.json['last_name'], request.json['email'], request.json['birth_date'], request.json['conferences'], request.json['activities'], request.json['tresor_hunt'], request.json['isUSTHB'], request.json['which_university'])
        except EmailAlreadyExistError as e:
            return jsonify({"error": str(e)})
        except InvalidActivityError as e:
            return jsonify({"error": str(e)})

        if (inserted):
            return jsonify({"success":"Paritcipant added successfully"})
        else:
            return jsonify({"error": "Can't add participant"})
api.add_resource(participant,'/register')


if __name__ == "__main__":
    app.run()
