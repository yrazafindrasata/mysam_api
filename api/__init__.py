from flask import Flask
from flask_cors import CORS
from flask_replicated import FlaskReplicated

from api.database import db
from api.blueprints import trip


def create_app(app_name='mysam_api'):
    app = Flask(app_name)
    app.config['READY'] = True
    app.config.from_pyfile('config/base.cfg')
    app.config.from_pyfile('config/local.cfg', silent=True)

    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    FlaskReplicated(app)

    app.register_blueprint(trip)

    return app
