

from pathlib import Path
import os
from .base_settings import *


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c305b704417038697acaa7eda5e2e3db063157d2d9e9344f87fef76bd7ec1e2c58348f628caa12e92ec28f1b7b1987a99077feee4cd66fd12c939ef68031384'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

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