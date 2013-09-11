from google.appengine.ext import db

class Subscriber(db.Model):
	email = db.StringProperty(multiline=False, required=True)
	insert_date = db.DateTimeProperty(auto_now_add=True)

class Gogodownloader(db.Model):
	ip = db.StringProperty(multiline=False, required=True)
	browser = db.StringProperty(multiline=False, required=True)
	referrer = db.StringProperty(multiline=False, required=True)
	download_date = db.DateTimeProperty(auto_now_add=True)