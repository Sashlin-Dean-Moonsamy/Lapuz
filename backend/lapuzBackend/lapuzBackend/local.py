from .settings import *


# SECURITY WARNING: keep the secret key used in production secret!
# Stored In Environment and generated using django.core.management.utils.get_random_secret_key method
SECRET_KEY = os.environ.get('LOCAL_SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
