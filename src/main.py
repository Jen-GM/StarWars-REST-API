"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Planet_favorite, Character_favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#GET for all the users
@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.filter().all()
    result = list(map(lambda user: user.serialize(), users))

    response_body = {
        "user": result
    }

    return jsonify(response_body), 200

#############################################     CHARACTERS FUNCTIONALITIES  ################################

#GET for all the characters
@app.route('/character', methods=['GET'])
def get_characters():
    characters = Character.query.filter().all()
    result = list(map(lambda character: character.serialize(), characters))
    
    response_body = {
        "character": result
    }

    return jsonify(response_body), 200

#GET for each character by ID
@app.route('/character/<int:id>', methods=['GET'])
def get_characters_byID(id):
    character = Character.query.get(id)
    print(character.serialize())
    result = {
        "personaje": character.serialize()
    }

    return jsonify(result), 200


#POST for adding favorite characters
@app.route('/character_favorite/<int:character_id>/<int:user_id>', methods=['POST'])
def post_favorite_character(character_id, user_id):
    favorite_character = Character_favorite(character_id=character_id, user_id=user_id)
    db.session.add(favorite_character)
    db.session.commit()
    result = {
    "Respuesta": "personaje favorito agregado"
    }
    return jsonify(result), 200

#DELETE the unwanted character
@app.route('/character_favorite/<int:user_id>/<int:character_id>', methods=['DELETE'])
def delete_character(user_id, character_id):
    delete_favorite_character = Character_favorite.query.filter_by(user_id=user_id, character_id=character_id).first()
    if delete_favorite_character is None:
        return jsonify({"Respuesta": "No existe el personaje a eliminar"})
    db.session.delete(delete_favorite_character)
    db.session.commit()

    result = {
    "Respuesta": "personaje favorito eliminado"
    }
    return jsonify(result), 200

#GET for the favorites characters
@app.route('/character_favorite/<int:user_id>', methods=['GET'])
def favorite_character(user_id):
    Fav_Character= Character_favorite.query.filter_by(user_id=user_id)
    result = list(map(lambda favorite: favorite.serialize(), Fav_Character))

    result = {
        "favorite_character" : result
    }

    return jsonify(result), 200

#############################################     PLANETS FUNCTIONALITIES  ################################

#GET for all the planets
@app.route('/planet', methods=['GET'])
def get_planet():
    planets = Planet.query.filter().all()
    result = list(map(lambda planet: planet.serialize(), planets))
    
    response_body = {
        "planet": result
    }

    return jsonify(response_body), 200

#GET for each planet by ID
@app.route('/planet/<int:id>', methods=['GET'])
def get_planet_byID(id):
    planet = Planet.query.get(id)
    print(planet.serialize())
    result = {
        "planeta": planet.serialize()
    }

    return jsonify(result), 200

#POST for adding favorite planets
@app.route('/planet_favorite/<int:planet_id>/<int:user_id>', methods=['POST'])
def post_favorite_planet(planet_id, user_id):
    favorite_planet = Planet_favorite(planet_id=planet_id, user_id=user_id)
    db.session.add(favorite_planet)
    db.session.commit()
    
    result = {
    "Respuesta": "Planeta favorito agregado"
    }
    return jsonify(result), 200

#DELETE the unwanted planet *****
@app.route('/planet_favorite/<int:user_id>/<int:planet_id>', methods=['DELETE'])
def delete_planet(user_id, planet_id):
    delete_favorite_planet = Planet_favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if delete_favorite_planet is None:
        return jsonify({"Respuesta": "No existe el planeta a eliminar"})
    db.session.delete(delete_favorite_planet)
    db.session.commit()

    result = {
    "Respuesta": "Planeta favorito eliminado"
    }
    return jsonify(result), 200 

#GET for the favorites planets
@app.route('/planet_favorite/<int:user_id>', methods=['GET'])
def get_favorite_planet(user_id):
    Fav_Planet= Planet_favorite.query.filter_by(user_id=user_id)
    result = list(map(lambda favorite: favorite.serialize(), Fav_Planet))

    result = {
        "favorite_planet" : result
    }

    return jsonify(result), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
