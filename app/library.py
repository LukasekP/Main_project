from flask import Flask, render_template, request, Blueprint
bp = Blueprint('library', __name__, url_prefix='/library', template_folder='../templates', static_folder='../static')
@bp.route('/')
def index():
    return render_template("library.html")