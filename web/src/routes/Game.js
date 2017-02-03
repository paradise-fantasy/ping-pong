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
    setTimeout(() => {
      this.props.dispatch({ type: 'MATCH_INTRO_OVER' });
    }, 5000);
  }

  gameEventListener(action) {
    switch (action.type) {
      case 'MATCH_OVER':
      case 'MATCH_CANCELLED':
      GameSocket.removeListener('GAME_EVENT', this.gameEventListener);
        setTimeout(() => {
          this.props.dispatch({ type: 'RESET_MATCH' })
          this.props.router.push('/');
        }, 5000);
        break;
    }
  }

  render() {
    const { game, player1, player2 } = this.props;

    let winner = {}, loser = {};
    if (game.state == 'over') {
      winner = game.score1 > game.score2 ? player1 : player2;
      loser = game.score1 > game.score2 ? player2 : player1;
    }

    return (
      <div className="Game">
        { game.state == 'starting' ?
          <div className="Game-starting">
            <div>
              <h1>Match Starting</h1>
              <h2>{player1.name}</h2>
              <h3>vs.</h3>
              <h2>{player2.name}</h2>
            </div>
          </div>
          : null
        }

        { game.state == 'started' ?
          <div className="Game-started">
            <div className="Game-player player-1">
              <div>
                <h1 className="Game-player-name">{player1.name}</h1>
                <h1 className="Game-player-score">{game.score1}</h1>
              </div>
            </div>
            <div className="Game-player player-2">
              <div>
                <h1 className="Game-player-name">{player2.name}</h1>
                <h1 className="Game-player-score">{game.score2}</h1>
              </div>
            </div>
          </div>
          : null
        }

        { game.state == 'over' ?
          <div className="Game-over">
            <div>
              <h1>Winner!</h1>
              <h2>{winner.name}</h2>
              <div className="Game-over-score">
                <span>{game.score1}</span>
                <span>-</span>
                <span>{game.score2}</span>
              </div>
            </div>
          </div>
          : null
        }

        { game.state == 'cancelled' ?
          <div className="Game-cancelled">
            <h1>Match Cancelled</h1>
          </div>
          : null
        }
      </div>
    )
  }
}

Game.defaultProps = {
  player1: {
    name: 'Player 1'
  },
  player2: {
    name: 'Player 2'
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
