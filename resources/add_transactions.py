from flask_restful import Resource
from flask import request
from app import bc


class AddTransaction(Resource):
    def post(self):
        values = request.get_json()
        required = ['sender', 'recepient', 'amount']
        if not all(k in values for k in required):
            return "Missing data", 400
        index = bc.add_transaction(values['sender'], values['recepient'], values['amount'])
        response = {
            'message': f'Transaction will be added to the block: {index}'
        }
        return response, 201
