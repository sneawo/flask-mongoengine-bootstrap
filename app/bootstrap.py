import uuid

import structlog
from flask import Flask, request, g
from flask_mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix

from .api import api_blueprint


logger = structlog.get_logger(__name__)
mongo = MongoEngine()


def init_app(config_obj=None, **kwargs):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)  # http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups

    if config_obj:
        app.config.from_object(config_obj)
    app.config.update(kwargs)

    mongo.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix='/')

    @app.before_request
    def set_logger():
        """Set request_id in logger to group log messages by request."""
        g.request_id = request.headers.get('Request-Id', str(uuid.uuid4()))
        log = logger.new(request_id=g.request_id)
        log.info(endpoint=request.endpoint, url=request.url)

    return app
