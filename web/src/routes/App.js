import React, { Component } from 'react';
import StatusBar from '../components/StatusBar';

class App extends Component {
  render() {
    return (
      <div className="App">
        <StatusBar />
        {this.props.children}
      </div>
    );
  }
}

export default App;
