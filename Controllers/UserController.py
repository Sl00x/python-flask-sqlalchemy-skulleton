from database import db
from Models import User

class UserController:
    def addUser(self, name, email):
        db.create_all()
        user = User.User(name, email)
        db.session.add(user)
        db.session.commit()
        


