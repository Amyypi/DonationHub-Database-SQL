from DonationHub import db

# Table of users
class users(db.Model):
	username = db.Column(db.String(50), primary_key=True)
	password = db.Column(db.String(50))
	email = db.Column(db.String(50))