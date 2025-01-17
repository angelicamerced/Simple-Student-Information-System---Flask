from os import getenv

SECRET_KEY = getenv('SECRET_KEY')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USERNAME')
DB_PASS = getenv('DB_PASS')

CLOUD_NAME = getenv('CLOUD_NAME')
API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
