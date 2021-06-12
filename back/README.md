pip3 install flask
****************************
pip3 install Flask-PyMongo
****************************
pip3 install Flask-Cors
****************************
pip3 install flask-restful
****************************

#API Calls

## Participant
the endpoint is '/register'
### POST
an example of json files taken for a participant POST request
```json
{
    "first_name":"first name",
    "last_name":"name",
    "email":"email1@gmail.com",
    "status":"student",
    "date_of_birth":"02/11/1998",
    "conferences":{
        "panel1": true,
        "panel2":true,
        "conference1": true,
        "conference2": false,
        "conference3": false
    },
    "workshops":{
        "python": true,
        "godot": false
    },
    "chasse_au_tresor":true,
    "battle_graphique":false,
    "team_emails":[
        "email2@gmail.com",
        "email3@gmail.com",
        "email4@gmail.com"
    ]
}
```

## Feedback
the endpoint is '/feedback'
### POST
an example of json files taken for a feedback POST request
```json
{
    "name":"aymen",
    "email":"aymenkhouas@gmail.com",
    "message":"this is my feedback",
}
```
