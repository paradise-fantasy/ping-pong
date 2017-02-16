import React, { Component } from 'react';
import ping_pong from '../../assets/images/ping_pong.svg';

import './style.css';


class PageHeader extends Component {
  render() {
    return (
    <div className="PageHeader">
        <div className="PageHeader-overlay">
        </div>
            <div className="PageHeader-header">
                <img src={ping_pong} className="PageHeader-logo" alt="logo" />
                <h2>{this.props.headerText}</h2>
            </div>
        </div>
    );
  }
}

PageHeader.defaultProps = {
    headerText: 'Komstek Ping Pong League'
}

export default PageHeader;
