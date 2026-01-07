student_login/

app.py── templates/
    login.html
        static/
        style.css
    script.js
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "student" and password == "1234":
            return "Login Successful 🎉"
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

* {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

body, html {
    height: 100%;
    overflow: hidden;
}

/* Animated Background */
.background {
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(-45deg, #1d2671, #c33764, #1d2671);
    background-size: 400% 400%;
    animation: gradient 8s ease infinite;
    z-index: -1;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Login Box */
.login-box {
    width: 300px;
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    margin: auto;
    margin-top: 15%;
    border-radius: 10px;
    text-align: center;
    color: white;
    backdrop-filter: blur(10px);
}

.login-box input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: none;
    border-radius: 5px;
}

.login-box button {
    width: 100%;
    padding: 10px;
    background: #ff9800;
    border: none;
    color: white;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
}
document.addEventListener("mousemove", (e) => {
    const box = document.querySelector(".login-box");
    let x = (window.innerWidth / 2 - e.pageX) / 20;
    let y = (window.innerHeight / 2 - e.pageY) / 20;
    box.style.transform = `rotateX(${y}deg) rotateY(${x}deg)`;
});
