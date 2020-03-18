from app import *
from flask import jsonify, request


@app.route('/')
def hw():
    return "hello world"


@app.route('/mine', methods=['GET'])
def main():
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
    return jsonify(response), 201


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recepient', 'amount']
    if not all(k in values for k in required):
        return "Missing data", 400
    index = bc.add_transaction(values['sender'], values['recepient'], values['amount'])
    response = {
        'message': f'Transaction will be added to the block: {index}'
    }
    return jsonify(response), 201


def full_chain():
    response = {
        'chain': bc.chain,
        'length': len(bc.chain)
    }
    return jsonify(response), 200
