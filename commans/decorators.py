import jwt
from flask import request
from flask_restx import abort

from constans import SECRET, ALGO
from service.user import user_object


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user_data = jwt.decode(token, SECRET, algorithms=[ALGO])
            user = user_object.get_user_by_username(user_data.get('username'))
            role = user.role
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        if role != "admin":
            abort(403)
        return func(*args, **kwargs)

    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[ALGO])
            print(jwt.decode(token, SECRET, algorithms=[ALGO]))
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper
