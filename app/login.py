from flask import Blueprint, request ,render_template, redirect, flash, url_for

from app.db import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        command = "SELECT username from users where username = ? and password = ?"
        result = db_execute(command, (username, password))
        if result:
            flash('Úspěšné přihlášení.', 'success')
            return render_template("index.html", username=username, password=password)
        else:
            flash('Špatné jméno nebo heslo.', 'danger')

    return render_template("login.html")




@bp.route('/users')
def user_list():
    command = "SELECT username, password FROM users"
    result = db_execute(command)
    return render_template("user.html", result=result)