import os
basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig:

    APPLICATION_ROOT = "/"
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_SECURE = True 
    SECRET_KEY = ""
    DEBUG = False 
    DATABASE_URI = ""
    DATABASE_NAME = ""
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    TESTING = False
    EMAIL = ""
    EMAIL_PASSWORD = ""

class ProductionConfig(AppConfig):

    DATABASE_URI = "./app/database/app-db.db"
    DATABASE_INIT = "./database/init.sql"
    DATABASE_NAME = "app-db.db"
    SECRET_KEY = ""
    DB_USERNAME = None
    DB_PASSWORD = None

class DevelopmentConfig(AppConfig):

    DATABASE_URI = "./app/database/test-db.db"
    DATABASE_INIT = "./database/test-init.sql"
    DATABASE_NAME = "test-db.db"
    SECRET_KEY = "ib7a3Ff382u98LU%8h3o_3yihr.13QQW3489uhonof8dho123155u98yihbka"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"

class TestConfig(AppConfig):
    
    HOST = "0.0.0.0"
    PORT = 3000
    DATABASE_URI = "./app/database/test-db.db"
    DATABASE_INIT = "./database/test-init.sql"
    DATABASE_NAME = "test-db.db"
    SECRET_KEY = "ib7a3Ff382u98LU%8h3o_3yihr.13QQW3489uhonof8dho123155u98yihbka"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False