import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "8000")
os.environ.setdefault("SECRET_KEY", "random_key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")
