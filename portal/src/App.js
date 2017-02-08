import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
import RegisterForm from './RegisterForm';
import logo from './logo.svg';
import './App.css';

class App extends Component {


  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>

        <Col md={8} mdOffset={2} >
            <RegisterForm />
        </Col>

      </div>
    );
  }
}

export default App;
