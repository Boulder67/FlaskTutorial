from werkzeug.security import safe_str_cmp
from models.user_models import UserModel
# users = [
#
#         User(1, 'sam','abcd')
#         # {
#         #
#         #         'id': 1,
#         #         'username': 'sam'
#         #         'password': 'abcd'
#         # }
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}
# username_mapping = { 'sam':{
#
#             'id': 1,
#             'username': 'sam'
#             'password': 'abcd'
#          }
#  }
# userid_mapping = { 1: {
#
#             'id': 1,
#             'username': 'sam'
#             'password': 'abcd'
#          }
#  }

# Authenticate users login
def authenticate(username, password):
    #user = username_mapping.get(username,None)
    user = UserModel.find_by_username(username)
    #if user and user.password = password:
    if user and safe_str_cmp(user.password, password):
        #return {"Good Job": user}
        return user





def identity(payload):
    user_id = payload['identity']
    #return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)
