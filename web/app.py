from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from helpers import genReturn
from entrance import enter
from hubroom import hub
from improom import imp
from jarroom import jar
from bossroom import boss

app = Flask(__name__)
CORS(app)
api = Api(app)

class Cave(Resource):
  def post(self):
    # Get posted data
    postedData = request.get_json()

    # Assign posted data to variables 
    choice = postedData["choice"]

    if choice == "default":
      room_name = 'entrance'
      room_details = "Welcome to the cave of decisions.\n Will you enter the cave?"
      room_options = ["Look.", "Enter."]

      return jsonify(genReturn(200, "Succesfully returned default room", room_name, room_details, room_options))

    looked = postedData["looked"]
    room = postedData["room"]


    # Handle choices
    if room == "entrance": 
      return jsonify(enter(choice, looked))
    
    elif room == "hubroom":
      trap = postedData["trap"]
      return jsonify(hub(choice, looked, trap))

    elif room == "improom":
      stick = postedData["stick"]
      hp = postedData["hp"]
      approach = postedData["approach"]

      return jsonify(imp(choice, looked, stick, hp, approach))
    
    elif room == "jarroom":
      return jsonify(jar(choice))

    elif room == "bossroom":
      stick = postedData["stick"]
      hp = postedData["hp"]

      return jsonify(boss(choice, looked, stick, hp))


api.add_resource(Cave, '/cave')

if __name__=="__main__":
  app.run(host='0.0.0.0')