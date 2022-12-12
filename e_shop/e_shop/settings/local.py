from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(0rgszmpti0ewa*3#31jb+7s)i!@1!*cz2#0^nd6ockn$+j7ta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
 #  {
 #      'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
 #  },
 #  {
 #      'NAME': 'django.contrib.auth.password_validation.CommonPass#wordValidator',
 #  },
 #  {
 #      'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
 #  },
]
