from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config


# db 초기화
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # 설정
    app.config.from_object(config)

    # db 참조
    db.init_app(app)
    from .models import Person, Concept, DrugExposure, Death, ConditionOccurrence

    # api 초기화
    from .apis import api as api
    api.init_app(app)

    return app
