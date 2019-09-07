from flask import Flask
from flask import url_for
from flask import render_template
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import abort
from waitress import serve
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/notice')
def notice():
    return render_template("notice.html")


@app.route("/problems")
def problems():
    # return render_template("problems.html")
    return redirect(url_for('login'))


@app.route("/scoreboard")
def scoreboard():
    # return render_template("scoreboard.html")
    return redirect(url_for('login'))

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if not session.get('logged_in'):
            return render_template("login.html")
        else:
            flash("You are already logged in.");
    elif request.method == "POST":
        # print(request.form)
        if request.form['password'] == 'password' and request.form['username'] == 'username':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash("Login failed.")
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()


app.secret_key = os.urandom(12)
serve(app, host="0.0.0.0", port="80")
