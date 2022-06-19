from crypt import methods
from flask import Blueprint,request,current_app
from app.utils.response.response import create_response
from datetime import datetime

bp = Blueprint("status",__name__,url_prefix="/status")

@bp.before_app_first_request
def first_app_request():
    date = str(datetime.utcnow().strftime("%Y%m%d-%H%M%S"))
    mode = current_app.config["ENV"]
    current_app.logger.info(f"{date} - APP INITIALIZING AS {mode}")
    

@bp.before_app_request
def request_metadata():
    method = request.method
    base = request.base_url
    date = str(datetime.utcnow().strftime("%d/%m/%d-%H:%M:%S"))
    current_app.logger.info(f"{date} - {method}| {base}")


@bp.route("/app")
def app_status():
    payload = {"OK":1}
    return create_response(payload,200)


@bp.route("/database")
def database_status():
    payload = {"OK":1}
    return  create_response(payload,200)


