import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(filename='logs/app.log', level=logging.INFO)


@app.route('/')
def hello_world():
    app.logger.info(f"Received a request from {request.remote_addr}")
    return 'Hello, World from Flask with logging!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
