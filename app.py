from flask import Flask
from flask import url_for
from flask import render_template
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import abort
from passwd import *
from config import *
from passlib.hash import pbkdf2_sha256
import datetime
import os


# Create an engine for managing password
engine = create_engine(db_path, echo=True)

# Create a Flask application
app = Flask(__name__)
app.secret_key = os.urandom(12)


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


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        POST_SECRET = str(request.form['secret'])
        POST_EMAIL = str(request.form['email'])

        # Check if given information is valid
        try:
            if POST_PASSWORD != POST_SECRET:
                flash("Error: the passwords do not match.")
                raise ValueError
            if not is_vaild_email(POST_EMAIL):
                flash("Error: the email address is invalid.")
                raise ValueError
        except:
            return redirect(url_for('signup'))

        Session = sessionmaker(bind=engine)
        s = Session()

        # Hash the password
        POST_PASSWORD = pbkdf2_sha256.encrypt(POST_PASSWORD, rounds=200000, salt_size=16)

        try:
            s.add(User(POST_USERNAME, POST_PASSWORD, POST_EMAIL))

            # Write change to database
            s.commit()
        except:
            flash("Error: duplicate user or email.")
            return redirect(url_for('signup'))

        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if not session.get('logged_in'):
            return render_template("login.html")
        else:
            return redirect(url_for('index'))
    elif request.method == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()

        # Validate whether the username and password is registered
        try:
            account = s.query(User).filter_by(username=POST_USERNAME).first()
            result = pbkdf2_sha256.verify(POST_PASSWORD, account.password)
        except:
            result = False

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