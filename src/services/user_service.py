from data.users import User

def create_user(username: str, password: str) -> User:
    user = User()
    user.username = username
    user.password = password
    user.save()

    return user

def find_user_by_username(username: str) -> User:
    user = User.objects().filter(username=username).first()
    return user

