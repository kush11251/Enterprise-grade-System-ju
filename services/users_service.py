from models import User
from repositories import users_repository
class UsersService:
    def get_users(self):
        return users_repository.get_users()