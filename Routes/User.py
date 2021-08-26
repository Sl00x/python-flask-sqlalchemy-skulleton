
from Controllers.UserController import UserController
from flask import Blueprint

user_route = Blueprint("user_route",__name__)

@user_route.route('/')
def index():
    controller = UserController()
    controller.addUser("univex", "admibzeiorf")

    return "coucou hibou"
