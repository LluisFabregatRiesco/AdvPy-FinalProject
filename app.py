
from typing import Any
from flask import Flask, render_template
import os
import db_api


app = Flask(__name__)


@app.route('/')
def home() -> Any:
    return render_template('home.html')


@app.route('/soccer')
def soccer() -> Any:
    return render_template('soccer.html')


@app.route('/baseball')
def baseball() -> Any:

    db_api.insert_one({"Test": 5, "Test Again": 8})

    res = db_api.find_all({})

    print(res)

    return render_template('baseball.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
