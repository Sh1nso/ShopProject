import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
PWD_HASH_SALT = os.getenv('PWD_HASH_SALT')
PWD_HASH_ITERATIONS = int(os.getenv('PWD_HASH_ITERATIONS'))
SECRET = os.getenv('SECRET')
ALGO = os.getenv('ALGO')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
