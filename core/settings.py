import os
import socket
import core.secrets as secrets

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = secrets.SECRET_KEY

IN_PRODUCTION = False

DEBUG = False

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
    'importadorJamendo',
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

if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
            )[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip

MY_URL = get_lan_ip()

if DEBUG==True:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'http://'+MY_URL+':3000/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'estaticos')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

if IN_PRODUCTION:
    S3_URL = 'http://keoh-sfotypy.s3.amazonaws.com/'
    MEDIA_URL = S3_URL + 'media/'
else:
    if DEBUG == True:
        MEDIA_URL = '/media/'
    else:
        MEDIA_URL = 'http://'+MY_URL+':3000/media/'
        MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

if IN_PRODUCTION:

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = secrets.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = secrets.AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME = secrets.AWS_STORAGE_BUCKET_NAME
