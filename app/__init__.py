from flask import Flask, render_template

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] =    "database.sqlite"

@app.route("/")
def index():
    return render_template("index.html")
