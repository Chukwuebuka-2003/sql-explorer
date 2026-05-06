import os
from pathlib import Path
from .settings import *

# Path resolution
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
DEBUG = False
ALLOWED_HOSTS = ["*"] 

# Security and Auth URLs
CSRF_TRUSTED_ORIGINS = ["https://explorer.comradic.com", "http://explorer.comradic.com"]
LOGIN_REDIRECT_URL = "/explorer/"
LOGIN_URL = "/explorer/login/"

# WhiteNoise for Static Files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Database Configuration
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

# Turn off Vite Dev Mode to fix the "Vite isn't running" error
EXPLORER_VITE_DEV_MODE = False
DJANGO_VITE = {"default": {"dev_mode": False}}
