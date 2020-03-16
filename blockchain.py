import json
import hashlib
from time import time
from typing import Dict


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(proof=100, prev_hash=1)

    def new_block(self, proof, prev_hash=None) -> Dict:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'prev_hash': prev_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recepient, amount) -> int:
        self.current_transactions.append(
            {
                'sender': sender,
                'recepient': recepient,
                'amount': amount
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha3_256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
