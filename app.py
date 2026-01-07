from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Login page (GET)
@app.route("/")
def home():
    return render_template("login.html")

# Login check (POST)
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = sqlite3.connect("static/database.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return "login success"
    else:
        return "invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
