
from models.store import StoreModel
from flask_restful import Resource, reqparse

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('store',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def get (self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "store not found"} ,404


    def post (self,name):
        store = StoreModel.find_by_name(name)
        if store :
            return {'message': 'this store alredy exists'}
        store = StoreModel(name)
        store.save_to_db()
        return store.json()

    def delete (self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'store deleted.'}
        return {'message': 'store not found.'}, 404


class StoreList(Resource):
    def get (self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
    
