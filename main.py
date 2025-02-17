from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/addBook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        radio = request.form['radio']
        return render_template("base.html", name=name, description=description, radio=radio)
    return render_template("addBook.html")

@app.route('/odkaz', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template("user.html", username=username, password=password)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
