from flask import Flask

from .routes import main
from .config import AppConfig
from .database.postgre import db
from .apis import api
from .mail import mail
from .database.redisdb import rediska


def create_app(rebuild_db: bool):
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    app.register_blueprint(main)

    api.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    rediska.init_app(app)
    
    if rebuild_db:
        with app.app_context():
            from.database.postgre.models import User
            db.create_all()        

    return app
