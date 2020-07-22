from os import environ

class Config:
	DEBUG = environ.get("DEBUG").lower() == "true" if "DEBUG" in environ else True
	
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = environ.get('EMAIL_USER')
	MAIL_PASSWORD = environ.get('EMAIL_PASS')

	SECRET_KEY = environ.get('SECRET_KEY')
	REGISTRATION_KEY = environ.get('REGISTRATION_KEY')