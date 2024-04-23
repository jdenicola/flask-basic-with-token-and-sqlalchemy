import os

from dotenv import load_dotenv

dotenv_path = os.getcwd() + "/.flaskenv"
load_dotenv(dotenv_path=dotenv_path, override=False)


class Config:
    # Main Database settings
    DB_HOST = os.environ.get('DB_HOST')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_PORT = os.environ.get('DB_PORT', default=3306)
    DB_NAME = os.environ.get('DB_NAME')
