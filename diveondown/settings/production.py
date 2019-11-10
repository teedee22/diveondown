from .base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


ALLOWED_HOSTS = ['www.diveondown.com', 'diveondown.com', 'localhost']

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 120
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DOD_DB_NAME'),
        'USER': os.environ.get('DOD_DB_USER'),
        'PASSWORD': os.environ.get('DOD_DB_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# AWS
AWS_ACCESS_KEY_ID = os.environ['DOD_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['DOD_AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['DOD_AWS_STORAGE_BUCKET_NAME']
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://' + '.s3.amazonaws.com/' + 'media/'
# remove when hook up email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
# Mail settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['MG_HOST']
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['MG_ADDRESS']
EMAIL_HOST_PASSWORD =os.environ['MG_PASSWORD']
EMAIL_USE_TLS = True

RECAPTCHA_PUBLIC_KEY = os.environ['TD_RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['TD_RECAPTCHA_PRIVATE_KEY']
NOCAPTCHA = True
"""
try:
    from .local import *
except ImportError:
    pass
