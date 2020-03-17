from flask import Flask
from blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)
bc = Blockchain()
node_uid = str(uuid4()).replace('-','')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
