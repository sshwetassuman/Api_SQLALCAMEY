
from models.user import UserModel
# users = [User(1,'bob','asdf'), User(2,"shweta","shwe")]

# user_mapping = {u.username : u for u in users}
# userid_mapping = {u.id : u for u in users}

def auth (username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password :
        return user

def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)


# def auth (username, password):
#     user = user_mapping.get(username)
#     if user and user.password == password :
#         return user

# def identity(payload):
#     user_id = payload["identity"]
#     return userid_mapping.get(user_id)

    