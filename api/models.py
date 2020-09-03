import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER
# from api import jwt, bcrypt, db
# from flask_jwt_extended import (
#     jwt_required, create_access_token, get_jwt_identity, decode_token
# )


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('LOCAL_DATABASE_URI')
db = SQLAlchemy(app)

# print(app.config['SQLALCHEMY_DATABASE_URI'])
class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def encode_auth_token(self, user_id):
        """
            Generates the Auth Token
            :return: string
            """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.create_access_token(identity=payload)
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode_token(auth_token)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Student(db.Model):
    """
    Student Model for all the registered students
    """
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    progress = db.Column(db.String(20), default="Registered")
    # cv = db.Column(db.Integer, db.ForeignKey('cv.id'))
    student_details = db.Column(db.Text)


class Professors(db.Model):
    """
    Professors Model for all the registered professors
    """
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recommended_students = db.Column(db.Text)
    requirements = db.Column(db.Text)
    professor_details = db.Column(db.Text)


class Cv(db.Model):
    """
    Cv Model for all the cvs made by students
    """
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_edited = db.Column(db.DateTime)
    cv = db.Column(db.Text)
    comments = db.Column(db.Text)
    # owner = db.relationship('students', backref='cv', lazy=True)


class Roles(db.Model):
    """
    Roles Model for all the Roles available
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), default="Student")


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False


if __name__ == '__main__':
    # db.create_all()
    db.drop_all()
