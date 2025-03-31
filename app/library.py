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
    """Zobrazí hlavní stránku knihovny

    Požaduje přihlášení uživatele (@login_required).
    Vrací vyrenderovanou šablonu library.html.

    Returns:
        str: Vyrenderovaná HTML šablona library.html
    """
    command = "SELECT name, author, pages FROM books"
    books = db_execute(command)
    return render_template("library.html", books=books)


@bp.route('/addbook', methods=['GET', 'POST'])
@login_required
def addbook():
    """Přidá novou knihu do knihovny

    Požaduje přihlášení uživatele (@login_required).
    Pokud je metoda POST, přidá knihu do databáze.
    Vrací šablonu addbook.html.
    """
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        pages = request.form['pages']

        command = "INSERT INTO books (name, author, pages) VALUES (?, ?, ?)"
        db_execute(command, (name, author, pages))
        flash('Kniha byla úspěšně přidána!', 'success')
        return redirect(url_for('library.index'))

    return render_template('addbook.html')
