#
# Note: Deleting socket.SO_REUSEPORT is a hack:
# It forces greenlet to resolve to use SO_REUSEADDR
# rather than SO_REUSEPORT which is apparently required
# by the current image. Remove this and errors may occur.
#
import socket
del socket.SO_REUSEPORT

import eventlet
from flask import Flask
from flask_socketio import SocketIO
import sys

from game import Game

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on("connect")
def on_connect():
    print "client connected"

if __name__ == "__main__":
    # Start the game
    print "starting game"
    game = Game(socket=socketio)
    print "game set up"
    eventlet.spawn_n(game.start)
    print "game spawned"
    socketio.run(app, host='0.0.0.0')
