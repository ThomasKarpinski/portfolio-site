from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def navbar():
    return render_template("navbar.html")


if __name__ == "__main__":
    app.run(debug=True)
