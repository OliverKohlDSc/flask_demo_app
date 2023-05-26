# pip freeze > requirements.txt
# touch .gitingore
# git init
# git add .
# git commit -m "Initial commit"

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
