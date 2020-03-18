from flask_restful import Api
from app import app
from resources import *

api = Api(app)


def init():
    api.add_resource(Mine, '/mine')
    api.add_resource(AddTransaction, '/transaction/new')
    api.add_resource(Chain, '/chain')
