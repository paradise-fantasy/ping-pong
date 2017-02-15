import React, { Component } from 'react';
import { Col } from 'react-bootstrap';

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
                <RankedList />
            </Col>
        </div>

      </div>
    );
  }
}

export default App;
