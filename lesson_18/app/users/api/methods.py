from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.database import User

main = Blueprint('main', __name__, url_prefix='/')
users = Blueprint('users', __name__, url_prefix='/users')


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)


@users.route('/', methods=['GET', 'POST'])
def get_all_users():
    user = User.query.all()
    return render_template('all_users.html', users=user)


@users.route('/<int:user_id>', methods=['GET'])
def search_user_by_id(user_id):
    user = User.query.get(user_id)
    return render_template('search_user.html', user=user, search_id=user_id)
