
from typing import Any
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home() -> Any:
    return render_template('home.html')


@app.route('/soccer')
def soccer() -> Any:
    return render_template('soccer.html')


@app.route('/baseball')
def baseball() -> Any:
    return render_template('baseball.html')
