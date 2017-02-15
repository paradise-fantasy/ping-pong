import React, { Component } from 'react';
import { Col } from 'react-bootstrap';

import PageHeader from '../PageHeader';

import './style.css';

class NotFound extends Component {


  render() {
    return (
      <div className="NotFound">
        <PageHeader headerText="Komstek Ping Pong League" />
        <div className="NotFound-intro">
            <Col md={8} mdOffset={2} >
                <img src="http://www.skogoglandskap.no/imagearchive/stort_hovedtekstbilde_part-whole_Kulturmuinne_stein_kastesteiner_lunner.jpg" alt="404 Not Found"/>
                <h1>Vi har lett under hver eneste sten, men kunne desverre ikke finne siden du leter etter.</h1>
            </Col>
        </div>

      </div>
    );
  }
}

export default NotFound;
