import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
import RegisterForm from './RegisterForm';
import ping_pong from './ping_pong.svg';
import './App.css';

class App extends Component {


  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={ping_pong} className="App-logo" alt="logo" />
          <h2>Komstek Ping Pong League</h2>
        </div>
        <div className="Registration">
            <Col md={8} mdOffset={2} >
                <RegisterForm />
            </Col>
        </div>

      </div>
    );
  }
}

export default App;
