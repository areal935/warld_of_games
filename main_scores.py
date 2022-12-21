from flask import Flask, redirect, url_for, render_template
from utils import SCORES_FILE_NAME
app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            my_score = file.read()
        app.run()
        return render_template('1.html', SCORE=my_score)
    except Exception as e:
        return render_template('2.html', ERROR=e)


app.run(debug=True)
