from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("templates.html")


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']

    db = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database_name"
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO table_name (text) VALUES (%s)", (text,))
    db.commit()

    db.close()

    return "Text added to database successfully!"


if __name__ == "__main__":
    app.run(debug=True)
