from flask_restful import Resource
from app import bc, node_uid


class Mine(Resource):
    def get(self):
        last_block = bc.last_block
        last_proof = last_block['proof']
        proof = bc.proof_of_work(last_proof)
        bc.add_transaction(sender="0", recepient=node_uid, amount=1)

        prev_hash = bc.hash(last_block)
        block = bc.new_block(proof, prev_hash=prev_hash)

        response = {
            'message': 'A new block forged',
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'prev_hash': block['prev_hash']
        }
        return response, 201
