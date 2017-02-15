import React, { Component } from 'react';
import { Col, Row } from 'react-bootstrap';

import PageHeader from '../PageHeader';
import RankedList from '../RankedList';

import './style.css';


class App extends Component {


  render() {
    return (
      <div className="App">
        <PageHeader headerText="Komstek Ping Pong League" />
        <div className="App-intro">
            <Col md={8} mdOffset={2} >
                <Row>
                    <RankedList />
                </Row>
                <Row>
                    <h1>
                        Not yet a player?<br />
                        <a href="/register">Register here</a>
                    </h1>
                </Row>
            </Col>
        </div>

      </div>
    );
  }
}

export default App;
