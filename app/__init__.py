from flask import Flask, render_template 
from flask.ext.bootstrap import Bootstrap 
# from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy 
from config import config

bootstrap = Bootstrap()
# moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    # moment.init_app(app)
    db.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .ardu import ardu as ardu_bp
    app.register_blueprint(ardu_bp)

    from .api_1_0 import api as api_1_0_bp
    app.register_blueprint(api_1_0_bp)

    return app