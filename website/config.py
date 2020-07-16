# import os

class Config:
	DEBUG = False #True if os.environ.get('DEBUG') in ['true', 'True'] else False
	
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'noreply10665@gmail.com' #os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = 'abc10665' #os.environ.get('EMAIL_PASS')

	SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' #os.environ.get('SECRET_KEY')
	REGISTRATION_KEY = 'apma1650!' #os.environ.get('REGISTRATION_KEY')