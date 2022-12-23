from flask import Flask, render_template, request, session
import requests
from speech_recog import *
from pprint import pprint

app = Flask(__name__)
app.secret_key="login"
@app.route('/')
def login1():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        if (username == "admin" and password == "10235000"):
            session['email'] = username
            return render_template('dashboard.html', email=username)
        else:
                msg="invalid username/password"
                return render_template('login.html', msg=msg)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/controller')
def controller():
    return render_template('controller.html')

@app.route('/speech_recog')
def speech_recog():
    return render_template('index.html')
    
@app.route('/mic', methods=["POST"])
def mic():
    if request.method == "POST":
        print('I got clicked')

        mic = take_user_input().lower()
        print(mic)
        while True:
            return render_template('index.html', mic=mic)

app.run(debug=False, host='0.0.0.0')