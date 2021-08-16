

from pathlib import Path
import os
from .base_settings import *


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
with open(str(BASE_DIR) + r"/secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


ALLOWED_HOSTS = ['122.248.208.99', 'sigurdvidarsson.com', 'www.sigurdvidarsson.com', '127.0.0.1']


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'static'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'