import json

from flask import request, Blueprint, jsonify


import os


users_blueprint = Blueprint('users', __name__, url_prefix='/app/users')

users_path = os.getcwd()+'/app/users/mock_data/users.json'


@users_blueprint.route('/', methods=['GET'])
def get_users():
    with open(users_path) as f:
        data = json.load(f)
    return jsonify(data)


@users_blueprint.route('/search', methods=['GET'])
def search_user_by_id():
    args = request.args

    user_id = args.get("id", default=0, type=int)

    with open(users_path) as f:
        data = json.load(f)

    for user in data:
        if user_id == user['id']:
            return user
    else:
        return 'Пользователя с таким id не существует!'


@users_blueprint.route('/add', methods=['GET', 'POST'])
def add_user():
    args = request.args

    with open(users_path) as f:
        data = json.load(f)

        new_user = {'id': (max(int(i['id']) for i in data) + 1),
                    'first_name': args.get('first_name', default='', type=str),
                    'last_name': args.get('last_name', default='', type=str),
                    'age': args.get('age', default=0, type=int),
                    'programming_languages': args.get('programming_languages', default=[''])}

        data.append(new_user)

    with open(users_path, mode='w') as f:
        json.dump(data, f)

    return 'Пользователь добавлен!'


@users_blueprint.route('/update/<user_id>', methods=['GET', 'PATCH'])
def update(user_id):
    args = request.args

    with open(users_path) as f:
        data = json.load(f)

        new_values = {'id': user_id,
                      'first_name': args.get('first_name', default='', type=str),
                      'last_name': args.get('last_name', default='', type=str),
                      'age': args.get('age', default=0, type=int),
                      'programming_languages': args.get('programming_languages', default=[''])}

        for i in data:
            if i['id'] == int(user_id):
                index = data.index(i)
                data[index] = new_values

    with open(users_path, mode='w') as f:
        json.dump(data, f)

    return 'Данные пользователя обновлены!'
