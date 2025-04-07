from flask import Flask, render_template, request, Blueprint, flash, session, redirect, url_for
from app.login import login_required
from app.db import db_execute

"""
Blueprint pro knihovní část aplikace

Attributes:
    name: Název blueprintu ('library')
    url_prefix: Základní cesta pro všechny routy ('/library')
    template_folder: Cesta k šablonám (o úroveň výš v adresáři templates)
    static_folder: Cesta ke statickým souborům (o úroveň výš v adresáři static)
"""
bp = Blueprint('library', __name__,
               url_prefix='/library',
               template_folder='../templates',
               static_folder='../static')


@bp.route('/')
@login_required
def index():
    """Zobrazí knihy aktuálně přihlášeného uživatele"""
    user_id = session["id"]
    command = "SELECT name, author, pages FROM books WHERE user_id = ?"
    books = db_execute(command, (user_id,))
    return render_template("library.html", books=books)


@bp.route('/addbook', methods=['GET', 'POST'])
@login_required
def addbook():
    """Přidá novou knihu do knihovny

    Požaduje přihlášení uživatele (@login_required).
    Pokud je metoda POST, přidá knihu do databáze.
    Vrací šablonu addbook.html.
    """
    if 'user_id' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        pages = request.form['pages']
        user_id = session['id']

        command = "INSERT INTO books (name, author, pages, user_id) VALUES (?, ?, ?, ?)"
        db_execute(command, (name, author, pages, user_id))
        flash('Kniha byla úspěšně přidána!', 'success')
        return redirect(url_for('library.index'))

    return render_template('addbook.html')
