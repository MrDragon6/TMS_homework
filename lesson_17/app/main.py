import flask

from lesson_17.app.users.api.methods import users_blueprint


def create_app() -> flask.Flask:
    """
    Создает и конфигурирует приложение.
    """
    app = flask.Flask(__name__)

    app.register_blueprint(users_blueprint)

    return app
