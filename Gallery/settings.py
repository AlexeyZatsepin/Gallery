"""
Django settings for Gallery project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ze0ny_dc_p3s0unype&mjav^ap5lp3!qg63qtc=wqpu1b8-rod'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    'D:/Django_code/Gallery/templetes',
)
ALLOWED_HOSTS = []
APPEND_SLASH=False
# Application definition

INSTALLED_APPS = (
    'imagekit',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'albums',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'loginsys',
    #'django-php',
    #'south',
)
TEMPLATE_CONTEXT_PROCESSORS =(
  'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',

                             )
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Gallery.urls'

WSGI_APPLICATION = 'Gallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
PROJECT_ROOT = os.path.dirname(__file__)
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#   ('static', 'D:/Django_code/Gallery/static'),
#)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    "/Gallery",
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'Gallery/media')
MEDIA_URL = '/media/'
#MEDIA_ROOT = (
 #  'D:/Django_code/Gallery/Gallery/media'
#)
STATIC_ROOT = "D:/Django_code/Gallery/static"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)