# Python packages
import logging
from pprint import pprint

# External Packages
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt 

from .config import DevelopmentConfig

migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_class)
    print(app)
    # CORS(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    
    from .auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .student.views import student_bluerprint
    app.register_blueprint(student_bluerprint)
    return app

this_app = create_app()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    this_app.logger.handlers = gunicorn_logger.handlers
    this_app.logger.setLevel(gunicorn_logger.level)
    
if __name__ == '__main__':
    print(DevelopmentConfig)
    print( this_app)
    # this_app.run(debug=True)
    # db.create_all()
