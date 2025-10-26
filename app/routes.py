from flask import Blueprint, render_template

# Blueprint will use the package's templates folder (app/templates)
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # Render an HTML page using Jinja2 template
    return render_template("index.html", message="Hello, Flask!")
