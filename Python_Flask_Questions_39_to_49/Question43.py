"""Describe the process of connecting a flask app to SQLite database using SQLAIchemy."""

## Step 1: Install Required Packages:  pip install flask flask-sqlalchemy

##  Import Necessary Libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run(debug=True)


