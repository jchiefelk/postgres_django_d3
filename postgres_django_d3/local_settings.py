from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB_NAME', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'PORT': os.environ.get('POSTGRES_PORT', ''),
    }
}
