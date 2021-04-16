import os

# default
APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(APP_DIR)

PORT = '5000'
FLASK_DEBUG = False

# log
LOG_PATH = os.path.abspath(APP_DIR) + "/log"

# sqlalchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(
    user='xxxxxxxxxxxxxx',
    pw='xxxxxxxxxxxxxxxx',
    url='xxx.xxx.xxx.xxx',
    db='xxxxxxxxxxxxxxxx')

# swagger
# SWAGGER_UI_DOC_EXPANSION = 'full'