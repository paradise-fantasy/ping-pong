import React, { Component } from 'react';
import { connect } from 'react-redux';

import { socket as GameSocket } from '../game-socket'

class Game extends Component {
  constructor() {
    super();
    this.gameEventListener = this.gameEventListener.bind(this);
  }

  componentDidMount() {
    GameSocket.on('GAME_EVENT', this.gameEventListener);
  }

  gameEventListener(action) {
    switch (action.type) {
      case 'MATCH_OVER':
      case 'MATCH_CANCELLED':
        setTimeout(() => {
          GameSocket.removeListener('GAME_EVENT', this.gameEventListener);
          this.props.router.push('/');
        }, 3000)
        break;
    }
  }

  render() {
    return (
      <div className="Game">
        <div className="Game-player player-1">
          <div>
            <h1 className="Game-player-name">{this.props.player1.name}</h1>
            <h1 className="Game-player-score">{this.props.game.score1}</h1>
          </div>
        </div>
        <div className="Game-player player-2">
          <div>
            <h1 className="Game-player-name">{this.props.player2.name}</h1>
            <h1 className="Game-player-score">{this.props.game.score2}</h1>
          </div>
        </div>
      </div>
    )
  }
}

Game.defaultProps = {
  player1: {
    name: ''
  },
  player2: {
    name: ''
  },
  game: {
    score1: 0,
    score2: 0
  }
}

const mapStateToProps = state => {
  const props = {};

  if (state.game.player1) props.player1 = state.players.map[state.game.player1]; // Grab the full player info
  if (state.game.player2) props.player2 = state.players.map[state.game.player2]; // Grab the full player info

  return {
    ...props,
    game: state.game
  };
};

export default connect(mapStateToProps)(Game);
