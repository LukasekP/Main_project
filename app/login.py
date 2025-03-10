from click import command
from flask import Blueprint, request ,render_template, redirect, flash, url_for

from app import db
from app.db import db_execute

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {'pokuston': 'kouzelnik', 'admin': 'admin', 'student': 'student'}
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            flash('Logged in successfully.', 'success')
        else:
            flash('Login failed.', 'danger')
        return render_template("index.html", username=username, password=password)
    return render_template("login.html")

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validace vstupů
        if not username:
            flash('Uživatelské jméno je povinné.', 'error')
        elif not email:
            flash('Email je povinný.', 'error')
        elif not password:
            flash('Heslo je povinné.', 'error')
        elif password != confirm_password:
            flash('Hesla se neshodují.', 'error')
        elif username in USERS:
            flash('Uživatelské jméno je již obsazené.', 'error')
        else:
            # Uložení uživatele (prozatím do dictionary)
            USERS[username] = password
            flash('Registrace proběhla úspěšně!', 'success')
            return redirect(url_for('login.login'))

    return render_template('register.html')


@bp.route('/users')
def user_list():
    command = "SELECT username, password FROM users"
    result = db_execute(command)
    return render_template("user.html", result=result)