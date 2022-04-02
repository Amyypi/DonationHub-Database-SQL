from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#tell sqlalchemy where the database file is
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#initialize the database
db = SQLAlchemy(app)

@app.route('/')
def main():
	return render_template('DataDashboard.html')