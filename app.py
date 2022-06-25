from api.views import url_shortener
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(url_shortener.bp)

    return app


app = create_app()
