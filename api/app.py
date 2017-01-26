#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

players = [
    {
        'id': 1,
        'name': u'Haavard',
        'cardid': 60,
        'profile_picture': 'http://tinypic.org/picture/b234cda512',
        'rating': 1000
    },
    {
        'id': 2,
        'name': u'Raymi',
        'cardid': 70,
        'profile_picture': 'http://tinypic.org/picture/b231cfa512',
        'rating': 1000
    }
]

@app.route('/api/players', methods=['GET'])
def get_tasks():
    return jsonify({'players': players})



@app.route('/api/players/<int:player_cardid>', methods=['GET'])
def get_player(player_cardid):
    player = [player for player in players if player['cardid'] == player_cardid]
    if len(player) == 0:
        abort(404)
    return jsonify({'player': player[0]})

@app.route('/api/players', methods=['POST'])
def create_player():
    if not request.json or not 'name' in request.json:
        abort(400)
    player = {
        'id': players[-1]['id'] + 1,
        'name': request.json['name'],
        'cardid': request.json['cardid'],
        'profile_picture': request.json['profile_picture'],
        'rating': 1000
    }
    players.append(player)
    return jsonify({'player': player}), 201

@app.route('/api/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'cardid' in request.json and type(request.json['cardid']) != unicode:
        abort(400)
    if 'profile_picture' in request.json and type(request.json['profile_picture']) is not unicode:
        abort(400)
    if 'rating' in request.json and type(request.json['rating']) != int:
        abort(400)
    player[0]['name'] = request.json.get('name', player[0]['name'])
    player[0]['cardid'] = request.json.get('cardid', player[0]['cardid'])
    player[0]['profile_picture'] = request.json.get('profile_picture', player[0]['profile_picture'])
    player[0]['rating'] = request.json.get('rating', player[0]['profile_picture'])
    return jsonify({'player': player[0]})


if __name__ == '__main__':
    app.run(debug=True)
