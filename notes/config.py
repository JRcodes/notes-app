import os

db_host = os.getenv("DB_HOSTNAME", "localhost")
db_name = os.getenv("DB_NAME", "notes")
db_username = os.getenv("DB_USERNAME", "notes")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT", "5432")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f"postgress://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
)
