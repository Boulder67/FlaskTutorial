import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT # for Athuntication
from Athuntication.security import authenticate, identity  # for Athuntication
from resources.user_resource import UserRegister, UsersList
from resources.item_resource import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///samdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'yousef'  # for Athuntication
api = Api(app)



jwt = JWT(app, authenticate, identity)  # for Athuntication
#items = [] We will use database instead


# class Item(Resource):
#     parser  = reqparse.RequestParser()
#     parser.add_argument('price',
#         type=float,
#         required=True,
#         help="This field cannot be left blanked"
#
#     )
#
#     @jwt_required()  # for Athuntication
#     def get(self, name):
#         # for item in items:
#         #     if item['name'] == name:
#         #         return item
#         #return 'item does not exist', 404
#         item = next(filter(lambda x: x['name'] == name, items),None)
#         return {'item': item}, 200 if item  else 404
#
#
#     def post(self,name):
#
#             #data = request.get_json()
#         if next(filter(lambda x: x['name'] == name, items),None):
#                  return {'message': "An item with name '{}' already exist".format(name)}, 400
#         data = Item.parser.parse_args()
#
#         #data = request.get_json()
#         item = {'name':name, 'price': data['price']}
#         items.append(item)
#         return item, 201
#
#     def delete(self,name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': "Item '{}' Deleted".format(name)}
#
#     def put(self, name):
#         # parser  = reqparse.RequestParser()
#         # parser.add_argument('price',
#         #     type=float,
#         #     required=True,
#         #     help="This fies cannot be left blanked"
#         #
#         # )
#         #data = request.get_json()
#         data = Item.parser.parse_args()
#
#         item = next(filter(lambda x:x['name'] == name,items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item
#
# class ItemList(Resource):
#     def get(self):
#         return {'ItemsList': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UsersList,'/users')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')



if __name__ == '__main__':

    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
