from flask import Blueprint
from flask import render_template

bp = Blueprint("home", __name__)


@bp.route("/")
def index():
    return render_template("home/index.html")

@bp.route("/about")
def omnie():
    return render_template("home/o_mnie.html")