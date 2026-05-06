import os
from .settings import *  # noqa: F401, F403

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Static files - THIS PART FIXES THE ERROR
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") 

# WhiteNoise (for serving static files in production)
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}
