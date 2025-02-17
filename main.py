from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/addBook', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        name = request.form['user']
        description = request.form['heslo']
        radio = request.form['radio']
        return render_template("base.html", name=name, description=description, radio=radio)
    return render_template("addBook.html")

if __name__ == '__main__':
    app.run(debug=True)
