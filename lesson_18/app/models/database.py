import flask_sqlalchemy
import sqlalchemy as sa
from flask_login import UserMixin


db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = sa.Column(
        sa.Integer, 
        primary_key=True,
        autoincrement=True
    )
    username = sa.Column(sa.String(100), unique=True, nullable=False)
    password = sa.Column(sa.String(100), nullable=False)
