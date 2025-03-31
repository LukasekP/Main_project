from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")

"""Konfigurační nastavení Flask aplikace

Attributes:
    SECRET_KEY: Tajný klíč pro zabezpečení session cookies a dalších bezpečnostních funkcí
    DATABASE: Cesta k SQLite databázovému souboru
"""
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = "database.sqlite"


@app.route("/")
def index():
    """Obsluha kořenové route aplikace

    Zobrazuje domovskou stránku aplikace na základě šablony index.html

    Returns:
        str: Vyrenderovaná HTML šablona index.html
    """
    return render_template("index.html")