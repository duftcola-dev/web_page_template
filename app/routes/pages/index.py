from flask import  Blueprint,render_template, request,current_app
from app.utils.response.response import create_response


bp = Blueprint("index",__name__,url_prefix="/")

@bp.route("/")
def index():

    return render_template("index.html")