from user import User
from saveable import Saveable
from database import Database


class Admin(User, Saveable):

    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f"<Admin : {self.username}, Access : {self.access}"

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }
