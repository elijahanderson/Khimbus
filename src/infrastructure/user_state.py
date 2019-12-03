from data.users import User

active_account: User = None

def reload_account():
    global active_account
    if not active_account:
        return

    pass

############################################################################
# When creating a new user (from front-end), use:
# user_exists = user_service.find_user_by_username(username)
# if user_exists:
#     error_msg(f"ERROR: Account with username {username} already exists.")
# user_state.active_account = user_service.create_account(userame, password)
# success_msg(f"Created new user with id {state.active_account.id}.")
############################################################################