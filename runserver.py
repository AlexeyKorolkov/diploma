import api
from app import app

if __name__ == '__main__':
    api.init()
    app.run(host='127.0.0.1', port=5000)
