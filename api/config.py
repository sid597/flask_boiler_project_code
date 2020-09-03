import os
basedir = os.path.abspath(os.path.dirname(__file__))
mysql_local_base = os.getenv('LOCAL_DATABASE_URI')
database_name = 'local_database'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY= '2489Ysdf#RYAR(*#Q$)#@$WEHRFsdkfh*((#@$fj'
    JWT_ALGORITHM='HS256'
class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_DATABASE_URI')
class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")