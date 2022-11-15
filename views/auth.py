from flask import request
from flask_restx import Resource, Namespace, abort

from implemented import user_service
from service.jwt_service import jwt_object

auth_ns = Namespace('auth')


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        req_data = request.json
        username = req_data.get('username', None)
        password = req_data.get('password', None)
        if None in [username, password]:
            return abort(401)
        tokens = jwt_object.give_user_jwt_token(username, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(400)
        tokens = jwt_object.check_refresh_token(refresh_token)
        return tokens, 201


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        req_user = request.json
        if req_user is None:
            return 'Введите необходимые данные', 400
        username = req_user.get('username', None)
        password = req_user.get('password', None)
        if None in [username, password] or len(req_user) > 2:
            return 'Ошибка ввода данных', 400
        try:
            user = user_service.create(req_user)
            return f'Пользователь  создан.' \
                   f'Для активации аккаунта перейдите по ссылке /auth/accept/{int(user.id)}', 201
        except:
            return 'Ошибка ввода данных', 400


@auth_ns.route('/accept/<uid>')
class ActivateView(Resource):
    def get(self, uid):
        try:
            user_service.activate_account(uid)
            return 'Аккаунт успешно активирован', 201
        except Exception as e:
            return e, 400
