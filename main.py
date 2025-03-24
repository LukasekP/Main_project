from app import app, login, library
from app.db import create_db
from os import path

if __name__ == '__main__':
    print(app.config["DATABASE"])
    if not path.exists(app.config["DATABASE"]):
        create_db()
        print("inicializace database")

app.register_blueprint(login.bp)
app.register_blueprint(library.bp)
app.run(debug=True)

