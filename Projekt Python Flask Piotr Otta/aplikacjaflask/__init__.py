import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="administrator-piotr",
        DATABASE=os.path.join(app.instance_path, "baza_danych.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from aplikacjaflask import db

    db.init_app(app)

    from aplikacjaflask import logowanie, posty, routes

    app.register_blueprint(routes.bp)
    app.register_blueprint(logowanie.bp)
    app.register_blueprint(posty.bp)

    app.add_url_rule("/", endpoint="index")

    return app
