from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'al1^jq&vt8n9*+7z%eie&44p!vsx^khu$l)l^gk+-9*ngwd9rm'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
