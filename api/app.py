#!flask/bin/python
from flask import Flask, jsonify, abort, request
from database import DB

app = Flask(__name__)
db = DB()
url = 129.241.200.204

@app.route('/')
def index():
    return "Hello, World!"

players = [
    {
        'id': 1,
        'name': u'Haavard',
        'surname': u'Fagervoll',
        'cardid': 60,
        'profile_picture': 'http://tinypic.org/picture/b234cda512',
        'rating': 1000,
        'wins': 0,
        'games_played': 4
    },
    {
        'id': 2,
        'name': u'Raymi',
        'surname': u'Eldby',
        'cardid': 70,
        'profile_picture': 'http://tinypic.org/picture/b231cfa512',
        'rating': 1000,
        'wins': 4,
        'games_played': 4
    }
]

matches = [
    {
        'id': 1,
        'time': "15:32 24.01.2017",
        'player_1': {
            'id': 1,
            'score': 6
        },
        'player_2': {
            'id': 2,
            'score': 11
        },
        'winner_id': 2
        # 'scores': {
        #     [1,2,1,2,1,1,1,2,2,1,1,2,2,1,1,1,2,2]
        # }
    },
    {
        'id': 2,
        'time': "15:44 24.01.2017",
        'player_1': {
            'id': 1,
            'score': 8
        },
        'player_2': {
            'id': 2,
            'score': 11
        },
        'winner_id': 2
        # 'scores': {
        #     [1,2,1,2,1,1,1,2,2,1,1,2,2,1,1,1,2,2]
        # }
    }
]

@app.route('/api/matches', methods=['GET'])
def get_matches():
    return jsonify({'matches': matches})

@app.route('/api/matches', methods=['POST'])
def create_match():
    if not request.json or not 'winner' in request.json:
        abort(400)
    player_1 = request.json['player_1']['id']
    player_2 = request.json['player_2']['id']
    score_player_1 = request.json['player_1']['score']
    score_player_2 = request.json['player_2']['score']
    winner = request.json['winner_id']
    scores = jsonify(request.json['scores'])

    if db.createMatch(player_1,
        player_2,
        score_player_1,
        score_player_2,
        winner,
        scores):
        return jsonify({'result': True}), 201
    else:
        return jsonify({'result': False})

# @app.route('/api/matches', methods=['POST'])
# def create_match():
#     if not request.json or not 'time' in request.json:
#         abort(400)
#     match = {
#         'id': matches[-1]['id'] + 1,
#         'time': request.json['time'],
#         'player_1': request.json['player_1'],
#         'player_2': request.json['player_2']
#     }
#     matches.append(match)
#     return jsonify({'match': match}), 201

@app.route('/api/players', methods=['GET'])
def get_players():
    #return jsonify({'players': players})
    players = db.getAllPlayers()
    return jsonify(players)

@app.route('/api/players/cardid/<int:player_cardid>', methods=['GET'])
def get_player_card(player_cardid):
    #player = [player for player in players if player['cardid'] == player_cardid]
    #if len(player) == 0:
    #    abort(404)
    player = db.getPlayerFromCardId(player_cardid)
    if not player:
        abort(400)
    #return jsonify({'player': player[0]})
    return jsonify(player)

@app.route('/api/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    # player = [player for player in players if player['id'] == player_id]
    # if len(player) == 0:
    #     abort(404)
    # return jsonify({'player': player[0]})

    player = db.getPlayerFromPlayerId(player_id)
    if not player:
        abort(400)
    return jsonify(player)

@app.route('/api/players', methods=['POST'])
def create_player():
    # if not request.json or not 'name' in request.json:
    #     abort(400)
    # player = {
    #     'id': players[-1]['id'] + 1,
    #     'name': request.json['name'],
    #     'cardid': request.json['cardid'],
    #     'profile_picture': request.json['profile_picture'],
    #     'rating': 1000
    # }
    # players.append(player)
    # return jsonify({'player': player}), 201

    if not request.json or not 'cardid' and 'name' in request.json:
        abort(400)

    name = request.json['name']
    cardid = request.json['cardid']

    result = db.createPlayer(name, cardid)
    if "Error" in result:
        abort(400)
    return jsonify(result), 201

@app.route('/api/players/<int:player_cardid>', methods=['PUT'])
def update_player(player_cardid):
    player = [player for player in players if player['cardid'] == player_cardid]
    if len(player) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'cardid' in request.json and type(request.json['cardid']) != int:
        abort(400)
    if 'profile_picture' in request.json and type(request.json['profile_picture']) is not unicode:
        abort(400)
    if 'rating' in request.json and type(request.json['rating']) != int:
        abort(400)
    player[0]['name'] = request.json.get('name', player[0]['name'])
    player[0]['cardid'] = request.json.get('cardid', player[0]['cardid'])
    player[0]['profile_picture'] = request.json.get('profile_picture', player[0]['profile_picture'])
    player[0]['rating'] = request.json.get('rating', player[0]['rating'])
    return jsonify({'player': player[0]})

@app.route('/api/players/<int:player_cardid>', methods=['DELETE'])
def delete_task(player_cardid):
    player = [player for player in players if player['cardid'] == player_cardid]
    if len(player) == 0:
        abort(404)
    players.remove(player[0])
    return jsonify({'result': True})



if __name__ == '__main__':
    app.run(debug=True)
