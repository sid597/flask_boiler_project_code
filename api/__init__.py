# Python packages
import logging
from pprint import pprint

# External Packages
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from api.config import DevelopmentConfig
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity, decode_token
)

migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class=DevelopmentConfig):
    print('Inside create app')
    app = Flask(__name__)
    print("configuration all set")
    app.config.from_object(config_class)

    # CORS(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from .student.routes import student_bp
    app.register_blueprint(student_bp)
    return app


this_app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    this_app.logger.handlers = gunicorn_logger.handlers
    this_app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    print(DevelopmentConfig)
    print(this_app)
    # this_app.run(debug=True)
    # db.create_all()
