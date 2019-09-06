from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/notice')
def notice():
    return render_template("notice.html")

@app.route("/problems")
def problems():
    return render_template("problems.html")

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

app.run(host="0.0.0.0", port="8080")