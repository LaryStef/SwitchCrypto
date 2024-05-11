from flask import Flask

from .routes import main
from .config import AppConfig
from .database.postgre import db
from .apis import api
from .mail import mail
from .database.redis import redis_client


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    app.register_blueprint(main)
    
    api.init_app(app)
    db.init_app(app)
    redis_client.init_app(app)
    mail.init_app(app)

    # with app.app_context():
    #     from .database.models import User
    #     db.create_all()        

    return app
