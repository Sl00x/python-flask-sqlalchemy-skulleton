from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
from routes import routes

def create_app():
    app = Flask(__name__)
    wsgi_app = app.wsgi_app
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/classy_db"
    db.init_app(app)
    for route in routes:
        app.register_blueprint(route['blueprint'], url_prefix=route['prefix'])
    return app 

if __name__ == '__main__':
    import os
    app = create_app()
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
