from Controllers.UserController import UserController
from flask import Blueprint, jsonify

home_route = Blueprint("home_route",__name__)

@home_route.route('/')
def index():
    return jsonify({
        "message" : "Bienvenue du skullapi",
        "version": 1.0,
        "author": "Alexis Quennehen",
        })
