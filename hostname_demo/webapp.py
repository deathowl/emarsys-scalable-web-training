import socket
from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def index():
    return Response(socket.gethostname())


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)

