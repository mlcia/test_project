import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Conf:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'Rmxhc2sgLSDQt9Cw0LzQtdGH0LDRgtC10LvRjNC90YvQuSDRhNGA0LXQudC80LLQvtGA0Lo='
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False