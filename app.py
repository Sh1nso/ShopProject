from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from config import Config
from setup_db import db
from views.admin import admin_ns
from views.auth import auth_ns
from views.payment import payment_ns
from views.product import product_ns

api = Api()
migrate = Migrate()


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db, directory='./ShopProject/migrations', )
    api.add_namespace(auth_ns)
    api.add_namespace(product_ns)
    api.add_namespace(payment_ns)
    api.add_namespace(admin_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
