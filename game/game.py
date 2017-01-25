# -*- coding: utf-8 -*-
from match import *
from player import *

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)


# # # # # # # # # # # # # # # # # # #
#           GAME SIMULATOR          #
# # # # # # # # # # # # # # # # # # #
match = Match()

player_1 = Player("Havard")
player_2 = Player("Raymi")

match.start(player_1, player_2)
socketio.emit("MATCH_STARTED")

print "New match started!\n"
while True:
    print match
    print "\nWho scores? (1/2)"

    player_number = -1
    while player_number < 1 or player_number > 2:
        if player_number != -1:
            print "Must be 1 or 2"
        try:
            player_number = int(raw_input())

        except ValueError:
            print "Invalid number!"

    try:
        match.update_score(player_number, 1)
        socketio.emit("NEW_SCORE", match)
    except MatchException, message:
        print message

    if match.state != GAME_IN_PROGRESS:
        break

socketio.emit("MATCH_OVER")
print "Match over!"
print match