#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
    parser  = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blanked!"
    )

    #parser  = reqparse.RequestParser()
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id, Please incude one"

    )
    # find item by its name
    # @classmethod
    # def find_by_name(cls, name):
    #     connection = sqlite3.connect('samdata.db')
    #     cursor = connection.cursor()
    #
    #     query =  "SELECT * FROM items WHERE name=?"
    #     result = cursor.execute(query, (name,))
    #     row = result.fetchone()
    #     connection.close()
    #
    #     if row:
    #         return {'item': {'name': row[0], 'price': row[1]}}
    @jwt_required()  # for Athuntication
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #return 'item does not exist', 404
        # item = next(filter(lambda x: x['name'] == name, items),None)
        # return {'item': item}, 200 if item  else 404
        # connection = sqlite3.connect('samdata.db')
        # cursor = connection.cursor()
        #
        # query =  "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     return {'item': {'name': row[0], 'price': row[1]}}
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': ' Item not found please refresh your memeory'}, 404


    def post(self,name):

            #data = request.get_json()
        #if next(filter(lambda x: x['name'] == name, items),None):
        if ItemModel.find_by_name(name):
                 return {'message': "An item with name '{}' already exist".format(name)}, 400
        data = Item.parser.parse_args()

        #data = request.get_json()
        item = ItemModel(name, data['price'],data['store_id'])




        #items.append(item)
        # Write item to the database
        # connection = sqlite3.connect('samdata.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(query, (item['name'], item['price']))
        #
        # connection.commit()
        # connection.close()

        #method fot post and put
        item.save_to_db()
        # try:
        #     item.insert(item)
        # except:
        #     return {"message": " An error occurred inserting the item. Please check the insert code"}, 500

        return item.json(), 201
    # @classmethod
    # def insert(cls, item):
    #     connection = sqlite3.connect('samdata.db')
    #     cursor = connection.cursor()
    #
    #     query = "INSERT INTO items VALUES(?, ?)"
    #     cursor.execute(query, (item['name'], item['price']))
    #
    #     connection.commit()
    #     connection.close()

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': "Item '{}' Deleted".format(name)}
        # global items
        # # items = list(filter(lambda x: x['name'] != name, items))
        # connection = sqlite3.connect('samdata.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()
        # return {'message': "Item '{}' Deleted".format(name)}

    def put(self, name):
        # parser  = reqparse.RequestParser()
        # parser.add_argument('price',
        #     type=float,
        #     required=True,
        #     help="This fies cannot be left blanked"
        #
        # )
        #data = request.get_json()
        data = Item.parser.parse_args()

        #item = next(filter(lambda x:x['name'] == name,items), None)
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])

        if item is None:

            item = ItemModel(name, data['price'],data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()
    #
    # @classmethod
    # def update(cls, item):
    #    connection = sqlite3.connect('samdata.db')
    #    cursor = connection.cursor()
    #
    #    query = "UPDATE items SET price=? WHERE name=?"
    #    cursor.execute(query, (item['price'], item['name']))
    #
    #    connection.commit()
    #    connection.close()
class ItemList(Resource):
    def get(self):
         return {'ItemsList':[ item.json() for item in ItemModel.query.all()]}
        # connection = sqlite3.connect('samdata.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'ID':row[0],'name': row[1], 'price':row[2]})
        #
        #
        # connection.close()
        # return {'ItemsList': items}
