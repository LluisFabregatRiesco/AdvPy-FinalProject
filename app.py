from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/soccer')
def soccer():
    return render_template('soccer.html')


@app.route('/baseball')
def baseball():
    return render_template('baseball.html')
