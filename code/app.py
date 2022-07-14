from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import auth, identity
from resources.user import UserRegister
from resources.item import Item, ItemList 
from resources.store import Store, StoreList
from models.store import StoreModel



app = Flask(__name__)

# app.config["SQLALCAMEY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)



jwt = JWT(app, auth, identity)

api.add_resource(Item, '/item/<string:name>')

api.add_resource(Store, '/store/<string:name>')

api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

api.add_resource(StoreList,"/stores")

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
    # from db import db
    # db.__init_app(app)
    # app.run (port = 5000, debug = True)