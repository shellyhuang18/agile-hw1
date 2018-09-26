from flask import Flask
import socket
app = Flask(__name__)

from app import routes
 
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)
