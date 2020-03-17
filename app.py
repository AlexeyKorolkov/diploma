from flask import Flask
from blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)
bc = Blockchain()
node_uid = str(uuid4()).replace('-', '')
