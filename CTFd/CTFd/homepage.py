from flask import Blueprint, render_template


homepage = Blueprint("homepage", __name__)


@homepage.route("/homepage")
def listing():
    return render_template("base.html")
