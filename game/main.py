#import eventlet
#eventlet.monkey_patch()
#
# import socketio
# from game import Game
#
# sio = socketio.Server()
# app = socketio.Middleware(sio)
#
# @sio.on('connect')
# def connect(sid, environ):
#     print('connect ', sid)
#
# @sio.on('disconnect')
# def disconnect(sid):
#     print('disconnect ', sid)
#
# if __name__ == '__main__':
#     # deploy as an eventlet WSGI server
#     game = Game(socket=sio)
#     eventlet.spawn_n(game.start)
#     eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

import gevent

from flask import Flask
from flask_socketio import SocketIO
import sys

from game import Game

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, async_mode='gevent')

@socketio.on("connect")
def on_connect():
    print "client connected"

if __name__ == "__main__":
    # Start the game
    game = Game(socket=socketio)
    gevent.spawn(game.start)
    socketio.run(app, host='0.0.0.0')
