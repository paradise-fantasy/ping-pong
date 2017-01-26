/**
 * Created by khrall on 26.01.2017.
 */
import GameSocket from '../game-socket'
import React, { Component } from 'react';

class Main extends Component {
  constructor() {
    super();
    this.removeListeners = this.removeListeners.bind(this);
    this.startNewGame = this.startNewGame.bind(this);
  }

  componentDidMount() {
    GameSocket.on('NEW_MATCH_STARTED', this.startNewGame);
  }

  startNewGame() {
    this.removeListeners();
    this.props.router.push('/game');
  }

  removeListeners() {
    GameSocket.removeListener('NEW_MATCH_STARTED', this.startNewGame);
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
            <tr>
              <td>1.</td>
              <td>Raymi</td>
              <td>1723</td>
              <td>(17-3)</td>
            </tr>
            <tr>
              <td>2.</td>
              <td>Håvard</td>
              <td>1541</td>
              <td>(11-5)</td>
            </tr>
            <tr>
              <td>3.</td>
              <td>Frederik</td>
              <td>1327</td>
              <td>(10-4)</td>
            </tr>
            <tr>
              <td>1.</td>
              <td>Raymi</td>
              <td>1723</td>
              <td>(17-3)</td>
            </tr>
            <tr>
              <td>2.</td>
              <td>Håvard</td>
              <td>1541</td>
              <td>(11-5)</td>
            </tr>
            <tr>
              <td>3.</td>
              <td>Frederik</td>
              <td>1327</td>
              <td>(10-4)</td>
            </tr>
            <tr>
              <td>1.</td>
              <td>Raymi</td>
              <td>1723</td>
              <td>(17-3)</td>
            </tr>
            <tr>
              <td>2.</td>
              <td>Håvard</td>
              <td>1541</td>
              <td>(11-5)</td>
            </tr>
            <tr>
              <td>3.</td>
              <td>Frederik</td>
              <td>1327</td>
              <td>(10-4)</td>
            </tr>
            <tr>
              <td>1.</td>
              <td>Raymi</td>
              <td>1723</td>
              <td>(17-3)</td>
            </tr>
            <tr>
              <td>2.</td>
              <td>Håvard</td>
              <td>1541</td>
              <td>(11-5)</td>
            </tr>
            <tr>
              <td>3.</td>
              <td>Frederik</td>
              <td>1327</td>
              <td>(10-4)</td>
            </tr>
            </tbody>
          </table>
        </div>

        <div className="Main-instructions">
          <marquee>
            <span>To start a ranked game, swipe each player's card on the RFID-reader one at a time.</span>
            <span>To start an unranked game, hold both score-buttons for 3+ seconds.</span>
            <span>To register a new player, click "Register".</span>
            <span>Thanks to all our supporters. Moms & Dads, bros and hoes &lt;3</span>
          </marquee>
        </div>
      </div>
    )
  }
}

export default Main;