import React, { Component } from 'react';

import './style.css';

import ping_pong from '../../assets/images/ping_pong.svg';

class ComingSoon extends Component {


  render() {
    return (
      <div className="ComingSoon">
            <h1>
                COMING SOON:<br />
                KOMSTEK PING PONG LEAGUE<br /><br />
                <img src={ping_pong} className="ComingSoon-logo" alt="logo" />
            </h1>
      </div>
    );
  }
}

export default ComingSoon;
