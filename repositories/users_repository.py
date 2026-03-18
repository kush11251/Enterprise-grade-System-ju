from models import User
from db import db
class UsersRepository:
    def get_users(self):
        return db.query(User).all()