import os
import core.secrets as secrets

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = secrets.SECRET_KEY

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'rest_framework',
    'artists',
    'tracks',
    'albums',
    'user_profile',
    'playlists',
    'genders',
    'usersong_counts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = secrets.DEVELOPMENT_DATABASE

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = 'http://localhost:3000/'

STATIC_ROOT = os.path.join(BASE_DIR, 'estaticos')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'http://localhost:3000/media/'

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

AUTH_USER_MODEL = 'user_profile.UserProfile'