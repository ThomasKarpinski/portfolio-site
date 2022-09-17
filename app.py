from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("templates.html")


@app.route("/portfolio")
def portfolio():
    return render_template("templates.html")


if __name__ == "__main__":
    app.run(debug=True)
