from flask import Flask


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if config:
        app.config.update(config)

    from .routes import bp
    app.register_blueprint(bp)

    return app
