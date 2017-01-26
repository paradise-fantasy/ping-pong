import GameSocket from '../game-socket'
import React, { Component } from 'react';

class Game extends Component {
  constructor() {
    super();

    this.state = {
      status: "Game in progress",
      player_1: {
        name: "",
        score: 0
      },
      player_2: {
        name: "",
        score: 0
      }
    };

    this.onMatchOver = this.onMatchOver.bind(this);
    this.onMatchCancelled = this.onMatchCancelled.bind(this);
    this.onPlayer1Score = this.onPlayer1Score.bind(this);
    this.onPlayer2Score = this.onPlayer2Score.bind(this);
    this.onPlayer1Revert = this.onPlayer1Revert.bind(this);
    this.onPlayer2Revert = this.onPlayer2Revert.bind(this);
    this.removeListeners = this.removeListeners.bind(this);
  }

  componentDidMount() {
    GameSocket.on('MATCH_OVER', this.onMatchOver);
    GameSocket.on('MATCH_CANCELLED', this.onMatchCancelled);
    GameSocket.on('PLAYER_1_SCORE_INC', this.onPlayer1Score);
    GameSocket.on('PLAYER_2_SCORE_INC', this.onPlayer2Score);
    GameSocket.on('PLAYER_1_SCORE_DEC', this.onPlayer1Revert);
    GameSocket.on('PLAYER_2_SCORE_DEC', this.onPlayer2Revert);
  }

  onMatchOver(match) {
    match.status = "Match is over, ";
    match.status += match.player_1.score > match.player_2.score ? match.player_1.name : match.player_2.name;
    match.status += " has won!";

    this.setState(match);
    setTimeout(() => {
      this.removeListeners();
      this.props.router.push('/');
    }, 5000);
  }

  onMatchCancelled() {
    this.setState({ status: 'Match cancelled!' });
    setTimeout(() => {
      this.removeListeners();
      this.props.router.push('/');
    }, 5000);
  }

  onPlayer1Score(match) {
    console.log(match);
    this.setState(match);
  }

  onPlayer2Score(match) {
    console.log(match);
    this.setState(match);
  }

  onPlayer1Revert(match) {
    console.log(match);
    this.setState(match);
  }

  onPlayer2Revert(match) {
    console.log(match);
    this.setState(match);
  }

  removeListeners() {
    GameSocket.removeListener('MATCH_OVER', this.onMatchOver);
    GameSocket.removeListener('MATCH_CANCELLED', this.onMatchCancelled);
    GameSocket.removeListener('PLAYER_1_SCORE_INC', this.onPlayer1Score);
    GameSocket.removeListener('PLAYER_2_SCORE_INC', this.onPlayer2Score);
    GameSocket.removeListener('PLAYER_1_SCORE_DEC', this.onPlayer1Revert);
    GameSocket.removeListener('PLAYER_2_SCORE_DEC', this.onPlayer2Revert);
  }

  render() {
    return (
      <div className="Game">
        <h1>This is a game</h1>
        <h2>{this.state.status}</h2>
        <p>{this.state.player_1.name}: {this.state.player_1.score}</p>
        <p>{this.state.player_2.name}: {this.state.player_2.score}</p>
      </div>
    )
  }
}
/*

GameSocket.on('NEW_MATCH_STARTED', (match) => {
  console.log('new match started', match)
});

GameSocket.on('MATCH_CANCELLED', (match) => {
  console.log('match cancelled', match)
});

GameSocket.on('PLAYER_1_JOINED', (player) => {
  console.log('player 1 joined', player)
});

GameSocket.on('GAME_OVER', (match) => {
  console.log('match over', match);
});

GameSocket.on('PLAYER_1_SCORE_INC', (match) => {
  console.log('player 1 scored', match);
});

GameSocket.on('PLAYER_2_SCORE_INC', (match) => {
  console.log('player 2 scored', match);
});

GameSocket.on('PLAYER_1_SCORE_DEC', (match) => {
  console.log('player 1 reverted point', match);
});

GameSocket.on('PLAYER_2_SCORE_DEC', (match) => {
  console.log('player 2 reverted point', match);
});

*/
export default Game;