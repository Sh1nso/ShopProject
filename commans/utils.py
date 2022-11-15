import jwt
from flask import request
from flask_restx import abort

from constans import SECRET, ALGO


def get_username_by_jwt():
    if 'Authorization' not in request.headers:
        abort(401)

    data = request.headers['Authorization']
    token = data.split("Bearer ")[-1]
    try:
        user_data = jwt.decode(token, SECRET, algorithms=[ALGO])
    except Exception as e:
        print(f"Traceback: {e}")
        abort(400)
    return user_data.get('username', None)
