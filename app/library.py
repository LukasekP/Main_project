from flask import Flask, render_template, request, Blueprint, flash, session, redirect, url_for

bp = Blueprint('library', __name__, url_prefix='/library', template_folder='../templates', static_folder='../static')
@bp.route('/')
def index():
    if not "username" in session:
        flash("Musíš ",warning)
        return redirect(url_for('login.login'))
    return render_template("library.html")