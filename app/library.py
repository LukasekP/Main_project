from flask import Flask, render_template, request, Blueprint, flash, session, redirect, url_for
from app.login import login_required
bp = Blueprint('library', __name__, url_prefix='/library', template_folder='../templates', static_folder='../static')
@bp.route('/')
@login_required
def index():
    return render_template("library.html")