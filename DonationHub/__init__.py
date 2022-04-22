from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize the flask app
app = Flask(__name__)
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#tell sqlalchemy where the database file is
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#initialize the database
db = SQLAlchemy(app)

from DonationHub import routes