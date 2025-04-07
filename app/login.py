from functools import wraps
from flask import Blueprint, request, flash, render_template, Flask, session, redirect, url_for
from app.db import db_execute

"""
Blueprint pro autentizační část aplikace

Attributes:
    name: Název blueprintu ('login')
    url_prefix: Základní cesta pro všechny routy ('/login')
"""
bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    """Zpracuje přihlašovací formulář"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Upravený dotaz - explicitně vybíráme potřebné sloupce
        command = "SELECT id, username, role, password FROM users WHERE username = ?"
        result = db_execute(command, (username,))

        if result:
            # Ověření hesla
            if result[0][3] == password:
                session['id'] = result[0][0]
                session['username'] = result[0][1]
                session['role'] = result[0][2]
                flash('Úspěšné přihlášení.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Špatné jméno nebo heslo.', 'danger')
        else:
            flash('Uživatel neexistuje.', 'danger')

    return render_template("login.html")

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Zpracuje registrační formulář

    Pro GET požadavek zobrazí registrační stránku.
    Pro POST požadavek ověří a uloží nového uživatele.

    Returns:
        str: Vyrenderovaná šablona register.html
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user = "user"
        if password != confirm_password:
            flash('Hesla se neshodují!', 'warning')
        else:
            try:
                command = "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)"
                db_execute(command, (username, email, password, user))
                flash('Registrace byla úspěšná!', 'success')
            except Exception as e:
                flash(f'Chyba při registraci: {str(e)}', 'danger')

    return render_template('register.html')



@bp.route('/logout')
def logout():
    """Odhlásí aktuálního uživatele

    Returns:
        Response: Přesměrování na přihlašovací stránku
    """
    session.pop('username', None)
    session.pop('role', None)
    flash("Odhlášen.")
    return redirect(url_for('login.login'))



def login_required(func):
    """Dekorátor pro kontrolu přihlášení uživatele

    Args:
        func: Funkce, kterou dekorátor obaluje

    Returns:
        function: Obalená funkce nebo přesměrování na login
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("sekce pro přihlášený uživatele", "warning")
            return redirect(url_for('login.login'))
        return func(*args, **kwargs)

    return wrapper


@bp.route('/users')
def user_list():
    """Zobrazí seznam všech uživatelů
    Returns:
        str: Vyrenderovaná šablona user.html s daty uživatelů
    """
    command = "SELECT username, password, role FROM users"
    users = db_execute(command)
    return render_template("user.html", users=users)