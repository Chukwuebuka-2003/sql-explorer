import os
from pathlib import Path
from .settings import *
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
DEBUG = False
ALLOWED_HOSTS = ["*"] 
# WhiteNoise for serving static files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# PostgreSQL connection
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
CSRF_TRUSTED_ORIGINS = [
    "https://explorer.comradic.com",
    "http://explorer.comradic.com",
]

LOGIN_REDIRECT_URL = "/explorer/"
LOGIN_URL = "/explorer/login/"


DJANGO_VITE = {
    "default": {
        "dev_mode": False,
    }
}
