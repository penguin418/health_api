from flask import Flask

from app.config import config


def create_app():
    app = Flask(__name__)

    # 설정
    app.config.from_object(config)

    return app
