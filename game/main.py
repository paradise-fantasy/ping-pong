from flask import Flask
from flask_socketio import SocketIO, emit
import sys

from game import Game

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@socketio.on("connect")
def on_connect():
    print "client connected"

if __name__ == "__main__":
    # Start the game
    game = Game(socket=socketio)
    game.start()
    socketio.run(app)
