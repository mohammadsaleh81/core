from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# ENVIRONMENT_CONF
load_dotenv()
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
FRONT_KEY = os.getenv('FRONT_KEY')

DEBUG = True


ALLOWED_HOSTS = ['bot.mobo.news', '157.90.106.158', '158.255.74.149',
                 'mindapi.mobo.news', '212.23.201.212', 'localhost', '*']


# APPS_CON
THIRD_PARTY_APPS = [
    'storages',
    'django_redis',
    'treebeard',
    'ckeditor',
    'ckeditor_uploader',
    'django_extensions',
    'rest_framework',
    'debug_toolbar',
    'drf_yasg',
    ]


PROJECTS_APPS = [
    'user',
    'organization',
    'taxonomy',
    'product',
]

# Application definition
INSTALLED_APPS = [
                     # 'unfold',
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.gis',
                     'django.contrib.sites',
                 ] + THIRD_PARTY_APPS + PROJECTS_APPS

AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'organization.middleware.SiteMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    'SHOW_COLLAPSED': True,
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}


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


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WSGI_APPLICATION = 'mobo.wsgi.application'
ROOT_URLCONF = 'mobo.urls'


# ELASTICSEARCH
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200'
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


def gettext(s): return s


LANGUAGES = (
    ('en', gettext('English')),
    ('fa', gettext('Persian')),
    ('ar', gettext('Arabic')),
)


AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = '5N1RFQN48Z90E8395KZY'
AWS_SECRET_ACCESS_KEY = 'B73oJKWkbpg9DQhL2B8MsnlHPRdBfDtkZ9kwiqvQ'
AWS_S3_ENDPOINT_URL = 'https://teh-1.s3.poshtiban.com'
AWS_STORAGE_BUCKET_NAME = 'cdn01.mobo.news'
AWS_S3_CUSTOM_DOMAIN = 'cdn.mobo.news'
AWS_S3_CUSTOM_DOMAIN_URL = 'cdn.mobo.news'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# STATICS
# STATICFILES_STORAGE = 'mobo.storage_backends.StaticStorage'
#STATIC_URL = '/static/'
#STATIC_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]

# settings.py

# URL to access static files
STATIC_URL = '/static/'

# Directory where static files are stored locally
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional directories for collectstatic to gather files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



# MEDIA
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'mobo.storage_backends.PublicMediaStorage'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'mobo.storage_backends.PrivateMediaStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "images/"


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240  # higher than the count of fields


# CELERY
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'


# API_KEYS
ARVANCLOUD_APIKEY = os.environ.get('ARVANCLOUD_APIKEY')
MERCHANT = os.environ.get('MERCHANT')
SANDBOX = False

KAVENEGAR_API_KEY = os.environ.get('KAVENEGAR_API_KEY')
OTP_CODE_LENGTH = 5

VENCY_CLIENT_ID = os.environ.get('VENCY_CLIENT_ID')
VENCY_CLIENT_SECRET = os.environ.get('VENCY_CLIENT_SECRET')

JIBIT_APIKEY = os.environ.get('JIBIT_APIKEY')
JIBIT_SECRETKEY = os.environ.get('JIBIT_SECRETKEY')

WP_PRODUCTS_API_KEY = os.environ.get('WP_PRODUCTS_API_KEY')

# CUSTOM_INCLUDE
AFFILIATE_PATH = {
    'mobile': 'https://mindapi.mobo.news/v1/mbt/',
    'accessory': 'https://mindapi.mobo.news/v1/acs/'
}

# GEOIP_PATH = os.path.join(BASE_DIR, 'geolite')


# JWT_CONF
ACCESS_TOKEN_LIFETIME = timedelta(days=9)
REFRESH_TOKEN_LIFETIME = timedelta(days=10)


# REST_FRAMEWORK_CONF
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #         'accounts.authentication.SafeJWTAuthentication',
    #     ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

CACHEOPS_REDIS = {
    'host': 'localhost', # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 1,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended
    'socket_timeout': 3,
}

CACHE_CONFIG = {
    'Product': {'timeout': 600},
    'ProductConfiguration': {'timeout': 600},
    'ProductVariant': {'timeout': 600},
    'Category': {'timeout': 600},
    'Brand': {'timeout': 600},
    'Tag': {'timeout': 600},
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User

    'product.Product': ('all', 60*60),
    'taxonomy.Category': ('all', 60*60),
    'taxonomy.Brand': ('all', 60*60),
}






if ENVIRONMENT == 'production':
    DEBUG = False
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
