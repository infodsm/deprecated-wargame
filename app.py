from flask import Flask
from flask import url_for
from flask import render_template
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import abort
from passwd import *
import datetime
import os


# Create an engine for managing password
engine = create_engine('sqlite:///passwd.db', echo=True)

# Create a Flask application
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
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()

        # Validate whether the username and password is registered
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()

        if result:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash("Error: username or password is invalid.")
            return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


app.secret_key = os.urandom(12)