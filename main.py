from flask import Flask
from flask import request
from flask import render_template
import requests

# setup flask
app = Flask(__name__)

swapi_url = "https://swapi.py4e.com/api/people"

# routes
@app.route('/characters')
def characters():

    return render_template("characters.html")


@app.route('/character_results', methods=["POST"])
def characters_results():
    """ show all star wars characters and their attributes """

    context = {}

    character_index = int(request.form.get("character_index"))

    results = requests.get(swapi_url).json()["results"]

    if len(results) > character_index:
        requested_character = results[character_index]
        context["character"] = requested_character

    

    return render_template("character_results.html", **context)


# def display_characters():
#     """ gets all star wars characters and returns an easily readable list """

#     results = requests.get(swapi_url).json()

#     characters = {}

#     for people in results.keys():
#         characters[people] = results[people]

#     return characters

# run flask
if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)