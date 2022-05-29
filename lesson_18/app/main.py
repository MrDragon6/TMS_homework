import os
import flask

from flask_login import LoginManager

from app.users.api.methods import main, users
from app.views.auth import auth
from app.models.database import db


def create_app() -> flask.Flask:
    """
    Создает и конфигурирует приложение.
    """
    app = flask.Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = '7d3jfg3k9dn50c8fn3k54hdn338nfe'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models.database import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(auth)

    return app
