# Statement for enabling the development environment
DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED     = True

CSRF_SESSION_KEY = os.environ.get('FLASK_CSRF_SESSION_KEY', 'secret')

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'secret')