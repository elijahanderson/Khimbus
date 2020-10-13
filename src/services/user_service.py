from mongoengine.queryset.visitor import Q

from data.users import User


def add_user(username: str, password: str, firstname: str, lastname: str, work_email: str, phone: str, job_title: str,
             supervisor: str, is_admin) -> User:
    user = User()
    user.username = username
    user.password = password
    user.firstname = firstname
    user.lastname = lastname
    user.work_email = work_email
    user.phone = phone
    user.job_title = job_title
    user.supervisor = supervisor
    user.is_admin = is_admin
    user.save()
    print('User saved!')
    return user


def find_user_by_username(username: str) -> User:
    user = User.objects(username=username).first()
    return user


def find_user_by_name(name: str) -> User:
    name = name.split(' ')
    if len(name) == 1:
        user = User.objects(Q(firstname=name[0]) | Q(lastname=name[0])).first()
    else:
        user = User.objects(Q(firstname=name[0]) & Q(lastname=name[1])).first()
    return user


def find_user_by_phone(phone: str) -> User:
    user = User.objects(phone=phone).first()
    return user


def find_user_by_email(email: str) -> User:
    user = User.objects(work_email=email).first()
    return user


def find_all_users():
    users = User.objects()
    return users


def repopulate_user(username, field, nvalue):
    user = User.objects(username=username).first()
    print('Updating...')
    if field == 'lastname':
        user.update(set__lastname=nvalue)
    elif field == 'firstname':
        user.update(set__firstname=nvalue)
    elif field == 'job_title':
        user.update(set__job_title=nvalue)
    elif field == 'work_email':
        user.update(set__work_email=nvalue)
    elif field == 'phone':
        user.update(set__phone=nvalue)
    elif field == 'supervisor':
        user.update(set__supervisor=nvalue)
    elif field == 'is_admin':
        user.update(set__is_admin=nvalue)
    else:
        return False

    user.reload()
    return user


def destroy_user(username):
    print('Deleting...')
    user = User.objects(username=username).first()
    if user:
        user.delete()
        print('Successfully deleted user!')
        return True
    return False
