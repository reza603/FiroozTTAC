from datetime import timedelta
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$r4i7=qy1up6b+^=a3f7hvdcpk=#4j^ct=%q1buyad!@_vklp!'

DEBUG = True

# ALLOWED_HOSTS = ['qrcode.firooz.com', '172.16.10.27', 'localhost', '127.0.0.1', '178.252.151.59']
ALLOWED_HOSTS = ['199.203.18.37','185.231.115.248', '172.16.10.27', 'localhost', '127.0.0.1', '178.252.151.59']


# default settings (optional)
# JALALI_DATE_DEFAULTS = {
#    # if change it to true then all dates of the list_display will convert to the Jalali.
#    'LIST_DISPLAY_AUTO_CONVERT': False,
#    'Strftime': {
#         'date': '%y/%m/%d',
#         'datetime': '%H:%M:%S _ %y/%m/%d',
#     },
#     'Static': {
#         'js': [
#             # loading datepicker
#             'admin/js/django_jalali.min.js',
#             # OR
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
#             # 'admin/js/main.js',
#         ],
#         'css': {
#             'all': [
#                 'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
#             ]
#         }
#     },
# }
LANGUAGE_CODE = 'fa'

import locale
locale.setlocale(locale.LC_ALL, "Persian_Iran.UTF-8")
# in other OS
# LANGUAGE_CODE = 'fa'

# import locale
# locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'crispy_forms',
'crispy_bootstrap4',
'rest_framework',
'rest_authtoken',
'maintenancemode',
'maintenance_mode',
'bootstrap4',
'uploader',
'order',
'barcode',
'jalali_date',
'inquiryHistory',
'customer',
'account',
'products',
'InspectionDetails',
'inspections',
'Shipping',
'ShippingDetails',
'Tasks',
'companies',
'clearcache',
]

MIDDLEWARE = [
'maintenance_mode.middleware.MaintenanceModeMiddleware',
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
'whitenoise.middleware.WhiteNoiseMiddleware',
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [
str(BASE_DIR.joinpath('Templates'))
],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
'django.template.context_processors.media',
],
},
},
]

WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {
'default': {
'ENGINE': 'mssql',
'NAME': 'amf_db',
'USER': 'sa',
'PASSWORD': 'amf@sqlDeveloper',
'HOST': '185.231.115.248',
'PORT': '1433',
'OPTIONS': {
'driver': 'ODBC Driver 17 for SQL Server',
},
}
}
# DATABASES = {
# 'default': {
# 'ENGINE': 'mssql',
# 'NAME': 'amf_db',
# 'USER': 'sa',
# 'PASSWORD': 'amf@sql2019',
# 'HOST': '172.16.10.27',
# 'PORT': '1433',
# 'OPTIONS': {
# 'driver': 'ODBC Driver 17 for SQL Server',
# },
# }
# }

AUTH_PASSWORD_VALIDATORS = [
{
'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
},
]

PASSWORD_HASHERS = [
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
'django.contrib.auth.hashers.Argon2PasswordHasher',
'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
'django.contrib.auth.hashers.ScryptPasswordHasher',
]

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fa'
import locale
locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
# TIME_ZONE = 'UTC'

USE_I18N = True

# USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'panel'
LOGOUT_REDIRECT_URL = 'panel'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
SITE_ROOT = PROJECT_ROOT

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
# os.path.join(SITE_ROOT, 'static'),
# )

TEMPLATE_DIRS = (
"C:/inetpub/wwwroot/TTACPORTAL/FiroozTTAC",
os.path.join(SITE_ROOT, 'Templates'),
)

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
),
}

SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5000),
'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
}