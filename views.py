from app import *
from flask import jsonify


@app.route('/mine', methods=['GET'])
def main():
    return "Mined a new block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return 'Made a new transaction'


def full_chain():
    response = {
        'chain': bc.chain,
        'length': len(bc.chain)
    }
    return jsonify(response), 200
