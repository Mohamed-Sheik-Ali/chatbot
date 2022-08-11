from flask import Flask
from flask_mongoengine import MongoEngine
import os
from .core.routes import core
from .core.middleware import Middleware
from . import settings
from dotenv import load_dotenv

load_dotenv()


def create_app():

    db = MongoEngine()

    app = Flask(__name__,  template_folder='./core/templates')
    app.wsgi_app = Middleware(app.wsgi_app)

    app.config['MONGODB_SETTINGS'] = {
        'db': 'testdb',
        'host': os.environ.get('MONGODB_URI')
    }

    db.init_app(app)

    app.config.from_object(settings.DevelopmentCfg)

    app.register_blueprint(core)

    return app
