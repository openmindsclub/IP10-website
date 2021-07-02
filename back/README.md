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
    "first_name": "first name",
    "last_name": "name",
    "email":"email1@gmail.com",
    "conferences":[
        "panel1",
        "panel2",
        "conference1",
        "conference2",
        "conference3"
    ],
    "workshops": "python",
    "battle_graphique": false,
    "tresor_hunt":true,
    "isUSTHB" : true,
    "which_university" : ""
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
