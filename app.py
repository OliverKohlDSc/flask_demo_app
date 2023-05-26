# Agenda:
# 1)
# Flask-App-Demo "Hallo Welt"

# 2)
# GIT -> GitHub

# 3)
# Cloud Shell

# 4)
# Deployment anstoßen
# App Services


# Befehle:

# pip freeze > requirements.txt
# touch .gitingore
# git init
# git add .
# git commit -m "Initial commit"
# git remote add origin https://github.com/OliverKohlDSc/flask_demo_app.git
# git push -u origin main


# Links
# https://github.com/OliverKohlDSc/flask_demo_app
# https://azure.microsoft.com/en-us/products/app-service/
# https://learn.microsoft.com/en-us/azure/app-service/

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
