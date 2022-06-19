import logging
from flask import Flask,request
from .routes.router import AppRouter
from .config import config

class App:
    """Creates the main app instance
    """

    def __init__(self) -> None:
        pass

    def __set_configuration(self,app:Flask,test)->Flask:
        """Set app configuration based on the current ENV

        Args:
            app (Flask): Flask class instance

        Returns:
            Flask: Flask class instance
        """
        if app.config["ENV"] == "development":
            app.config.from_object(config.DevelopmentConfig()) 
        if app.config["ENV"] == "production":
            app.config.from_object(config.ProductionConfig()) 
        if test:
            app.config["ENV"] == "test"
            app.config.from_object(config.TestConfig()) 
        
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
        
        return app 


    def init_app(self,test:bool=False)->Flask:
        """Initializes app
        """
        app_router = AppRouter()
        app = Flask(__name__)
        app = self.__set_configuration(app,test)    
        app = app_router.init_app(app)
        
        return app


