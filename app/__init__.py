from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from .app import main_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        "/metrics": make_wsgi_app()
    })

    return app
