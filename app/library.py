from flask import Flask, render_template, request, Blueprint, flash, session, redirect, url_for
from app.login import login_required

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
    return render_template("library.html")