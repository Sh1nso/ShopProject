from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> User:
        return self.session.query(User).get(uid)

    def get_all(self) -> User:
        return self.session.query(User).all()

    def get_user_by_username(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def activate_account(self, uid):
        user = self.get_one(uid)
        user.is_active = True
        self.session.add(user)
        self.session.commit()
        return ''

    def change_active(self, uid):
        user = self.get_one(uid)
        user.is_active = not user.is_active
        self.session.add(user)
        self.session.commit()
        return user

    def create(self, user_d: dict) -> User:
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid: int) -> str:
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
        return ''
