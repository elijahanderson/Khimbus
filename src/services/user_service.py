from src.data.users import User

def add_user(username: str, password: str) -> User:
    user = User()
    user.username = username
    user.password = password
    user.save()
    print('User saved!')
    return user

def find_user_by_username(username: str) -> User:
    user = User.objects(username=username).first()
    return user

def find_all_users():
    users = User.objects()
    return users
