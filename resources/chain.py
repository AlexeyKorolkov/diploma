from flask_restful import Resource
from app import bc


class Chain(Resource):
    def get(self):
        response = {
            'chain': bc.chain,
            'length': len(bc.chain)
        }
        return response, 200
