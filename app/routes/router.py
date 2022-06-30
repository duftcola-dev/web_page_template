from flask import Flask
from . app_status import bp as app_status_bp
from .pages.index import bp as app_index_bp
class AppRouter:

    def __init__(self) -> None:
        pass
        
    def init_app(self,app:Flask):
        """Register app blueprints and  endpoints

        Args:
            app (Flask): Flask class instance
        """
        
        app.register_blueprint(app_status_bp)
        app.register_blueprint(app_index_bp)
        return app