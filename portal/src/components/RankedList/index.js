import React, { Component } from 'react';
import { Table} from 'react-bootstrap';

import './style.css';

const HTTPS_ENABLED = !!process.env.REACT_APP_HTTPS_ENABLED;
const API_HOST = process.env.REACT_APP_API_HOST || 'localhost';
const API_PORT = process.env.REACT_APP_API_PORT || 8000;
const API_URL = `${HTTPS_ENABLED ? 'https' : 'http'}://${API_HOST}:${API_PORT}`;

function fetchPlayers() {
    return fetch (`${API_URL}/players/`, {
        method: "GET"
    })
    .then(res => res.json())
    .catch(err => console.log("Request failed", err))
}

//function sortPlayers(players) {
//}

class RankedList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            players: []
        }
        this.update = this.update.bind(this)
    }

    componentDidMount() {
        this.update()
        this.intervalId = setInterval(this.update, 5000)
    }

    componentWillUnmount() {
        clearInterval(this.intervalId);
    }

    update() {
        fetchPlayers()
        .then(
            players => players.sort((a, b) =>  b.rating - a.rating)
        )
        .then(
            players => this.setState({ players })
        )
    }


  render() {
    return (
      <div className="RankedList">
          <Table striped bordered condensed hover>
              <thead>
                  <tr>
                      <th>#</th>
                      <th>Name</th>
                      <th>Rating</th>
                  </tr>
              </thead>
              <tbody>
                  {
                      this.state.players.map((player, i) =>
                          <tr key={i}>
                              <td>{i+1}</td>
                              <td>{player.name}</td>
                              <td>{player.rating}</td>
                          </tr>
                     )
                  }
              </tbody>
          </Table>

      </div>
    );
  }
}

export default RankedList;
