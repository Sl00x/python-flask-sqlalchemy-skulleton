# python-flask-sqlalchemy-skulleton - Tutorial


### **How to add routes 💬**

To add routes it's really simple. You need to go in directory 📁`./Routes` and add your file like 📁`./Routes/Users.py`.
Now you can code your *blueprint*.

For example:
```python
from flask import Blueprint, jsonify

user_route = Blueprint("user_route",__name__)

@user_route.route('/')
def index():
    return jsonify({"github": "Sl00x"})
```
Now we need to add this 📑blueprint into 📁`./routes.js` to declare it.

Like this:
```python
#Declare your blueprint variable.
from Routes.User import user_route
from Routes.Home import home_route

#add to list
routes = [
    {"blueprint": user_route, "prefix": '/user'},
    {"blueprint": home_route, "prefix": '/'},
]
```
### **How to create controller 💬**
To create controller you need to go in directory 📁`./Controllers` and add your file like 📁`./Controller/UsersController.py`.
Example code:
```python
class UserController:
    def helloUser(self):
        print("hello github")

```
and add it to your routes 😼
Example to add controller in route:
```python
from flask import Blueprint, jsonify
from Controller.UserController import UserController

user_route = Blueprint("user_route",__name__)

@user_route.route('/', methods=['GET'])
def index():
    controller = UserController()
    controller.helloUser()
    return jsonify({"github": "Sl00x"})
```
### **To finish we need to add model for database 💬**

To create models you need to go in directory 📁`./Models` and add your file like 📁`./Models/User.py`.
Example code:
```python
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
```

Now for create controller with model in 📁`./Controller/UserController.py` 
```python
from database import db
from Models import User

class UserController:
    def addUser(self, name, email):
        db.create_all()
        user = User.User(name, email)
        db.session.add(user)
        db.session.commit()
```

Use this controller in 📁`./Routes/User.py` 

```python
from Controllers.UserController import UserController
from flask import Blueprint

user_route = Blueprint("user_route",__name__)

@user_route.route('/')
def index():
    controller = UserController()
    controller.addUser("github", "123")
    return "ok !"
```
