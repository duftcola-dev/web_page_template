import os
basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig:

    HOST = "0.0.0.0"
    PORT = 3000
    APPLICATION_ROOT = "/"
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_SECURE = True 
    SECRET_KEY = "*"
    DEBUG = False 
    DATABASE_URI = "*"
    DATABASE_NAME = "*"
    DB_USERNAME = "*"
    DB_PASSWORD = "*"
    TESTING = False
    EMAIL = "*"
    EMAIL_PASSWORD = "*"

class ProductionConfig(AppConfig):

    DATABASE_URI = "./app/db/app-db.db"
    DATABASE_INIT = "./db/init.sql"
    DATABASE_NAME = "app-db.db"
    SECRET_KEY = "*"
    DB_USERNAME = "*"
    DB_PASSWORD = "*"

class DevelopmentConfig(AppConfig):

    DATABASE_URI = "./app/db/test-db.db"
    DATABASE_INIT = "./db/test-init.sql"
    DATABASE_NAME = "test-db.db"
    SECRET_KEY = "*"
    DB_USERNAME = "*"
    DB_PASSWORD = "*"

class TestConfig(AppConfig):
    
    DATABASE_URI = "./app/database/test-db.db"
    DATABASE_INIT = "./database/test-init.sql"
    DATABASE_NAME = "test-db.db"
    SECRET_KEY = "*"
    DB_USERNAME = "*"
    DB_PASSWORD = "*"
    TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False