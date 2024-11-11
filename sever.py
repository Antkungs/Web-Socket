from flask import Flask
from flask_socketio import SocketIO,emit
from datetime import datetime
import time 
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    now = datetime.now()
    socketio.emit('response', 'You sent {0} {1}'.format(data,str(now)))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
