import calendar
import datetime
import jwt

from flask_restx import abort

from constans import SECRET, ALGO
from implemented import user_service


class JwtService:

    def give_user_jwt_token(self, username, password):
        user = user_service.get_user_by_username(username)
        if not user:
            return {"error": "Неверные учётные данные"}, 401

        user_pass = user_service.get_hash(password)
        if user_pass != user.password:
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "username": user.username
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def check_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])
        except Exception as e:
            abort(400)

        username = data.get("username")

        user = user_service.get_user_by_email(username)

        data = {
            "email": user.email
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201


jwt_object = JwtService()
