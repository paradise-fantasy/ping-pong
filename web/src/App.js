import React, { Component } from 'react';
import ninjaruto_font from './njnaruto.ttf';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-text-logo">
          <h1>The KomTek Table-Tennis League</h1>
        </div>

        <div className="App-scoreboard">
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

        <div className="App-instructions">
          <marquee>
            <span>To start a ranked game, swipe each player's card on the RFID-reader one at a time.</span>
            <span>To start an unranked game, hold both score-buttons for 3+ seconds.</span>
            <span>To register a new player, click "Register".</span>
            <span>Thanks to all our supporters. Moms & Dads, bros and hoes &lt;3</span>
          </marquee>
        </div>
      </div>
    );
  }
}

export default App;
