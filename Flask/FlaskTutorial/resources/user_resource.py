
#import sqlite3
from flask_restful import Resource, reqparse
from models.user_models import UserModel

# New users registeration
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                type=str,
                required=True,
                help="This field cannot be blank Please"
    )

    #parser = reqparse.RequestParser()
    parser.add_argument('password',
                type=str,
                required=True,
                help="This field cannot be blank"
    )

    def post(self):

       data = UserRegister.parser.parse_args()
       if  UserModel.find_by_username(data['username']):
            return {"message":"User name already exist"}, 400
       user = UserModel(data['username'], data['password']) # OR Just user = UserModel(**data)
       user.save_to_db()

        #connection = sqlite3.connect('samdata.db')
       # cursor = connection.cursor()
       #
       # query = " INSERT INTO users VALUES (NULL, ?, ?)"
       # cursor.execute(query,( data['username'], data['password']) )
       # connection.commit()
       # connection.close()

       return {"message": "User created sucessfully"}, 201
class UsersList(Resource):
    def get(self):

        return {'UsersList':[user.json() for user in UserModel.query.all()]}
        # connection = sqlite3.connect('samdata.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users"
        # result = cursor.execute(query)
        # users = []
        # for row in result:
        #     users.append({'ID': row[0], 'User Name':row[1]})
        #
        #
        # connection.close()
        # return {'ItemsList': users}
