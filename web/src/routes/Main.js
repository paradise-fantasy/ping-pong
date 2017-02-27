import React, { Component } from 'react';
import { connect } from 'react-redux';

import { socket as GameSocket } from '../game-socket';
import { getPlayers } from '../api';

class Main extends Component {
  constructor() {
    super();
    this.gameEventListener = this.gameEventListener.bind(this);
  }

  componentDidMount() {
    GameSocket.on('GAME_EVENT', this.gameEventListener);

    getPlayers().then(players => {
      this.props.dispatch({
        type: 'RECEIVE_PLAYERS',
        players
      });
    });
  }

  gameEventListener(action) {
    switch (action.type) {
      case 'NEW_MATCH_STARTED':
      case 'NEW_UNRANKED_MATCH_STARTED':
        GameSocket.removeListener('GAME_EVENT', this.gameEventListener);
        this.props.router.push('/game');
        break;
      default:
        return;
    }
  }

  render() {
    return (
      <div className="Main">
        <div className="Main-text-logo">
          <h1>The KomTek Table-Tennis League</h1>
        </div>

        <div className="Main-scoreboard">
          <table>
            <tbody>
            {
              this.props.players.sort((a, b) => b.rating - a.rating).map((player, i) =>
                <tr key={i}>
                  <td>{i+1}.</td>
                  <td>{player.name}</td>
                  <td>{player.rating}</td>
                  <td>{player.games_won} wins ({player.games_played} played)</td>
                </tr>
              )
            }
            </tbody>
          </table>
        </div>

        <div className="Main-instructions">
          <marquee>
            <span>To start a ranked game, swipe each player's card on the RFID-reader one at a time.</span>
            <span>To start an unranked game, hold both score-buttons for 3+ seconds.</span>
            <span>To register a new player, go to ping-pong.komstek.no!</span>
            <span>Thanks to all our supporters. Moms & Dads, bros and hoes &lt;3</span>
          </marquee>
        </div>

        { this.props.player1 ? // Check if player1 exists
          <div className="Main-player-joined-overlay">
            <h1>{this.props.player1.name} is ready to fight!</h1>
            <div className="Main-match-setup-expiration" />
          </div>
          : null
        }

      </div>
    )
  }
}

Main.defaultProps = {
  players: []
}

const mapStateToProps = state => {
  const props = {};

  if (state.game.player1) {
    props.player1 = state.players.map[state.game.player1]; // Grab the full player info
  }

  return {
    ...props,
    players: state.players.list,
    game: state.game
  };
};

export default connect(mapStateToProps)(Main);
