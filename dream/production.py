import os
from urllib.parse import urlparse
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['dreamstv0915.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', '%n@mp8p23k05*vcny1^7&7t!1m_sf9300+ogq3nv&h1shp2@6s')  
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

## Channels Specific
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "symmetric_encryption_keys": [SECRET_KEY],
    },
}
ASGI_APPLICATION = 'dream.routing.application'
