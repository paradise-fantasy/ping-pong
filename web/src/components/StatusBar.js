import React, { Component } from 'react';
import { connect } from 'react-redux';
import { v4 } from 'node-uuid';

import { socket } from '../game-socket';

class StatusBar extends Component {
  constructor() {
    super();
    this.receiveSocketAction = this.receiveSocketAction.bind(this);
    this.pushStatusMessage = this.pushStatusMessage.bind(this);
    this.clearMessageGroup = this.clearMessageGroup.bind(this);
  }

  componentDidMount() {
    socket.on('GAME_EVENT', this.receiveSocketAction);
  }

  componentWillUnmount() {
    socket.removeListener('GAME_EVENT', this.receiveSocketAction);
  }

  receiveSocketAction(action) {
    switch (action.type) {
      case 'PLAYER_NOT_REGISTERED':
        this.pushStatusMessage(`Your card id is: ${action.cardId}. It needs to be registered on ping-pong.komstek.no before you can use your card to play!`, 'cardId', 30000);
        break;
      case 'PLAYER_1_JOINED':
      case 'PLAYER_2_JOINED':
        this.clearMessageGroup('cardId');
        break;
      default:
        return;
    }
  }

  pushStatusMessage(text, group, timeout) {
    const id = v4();
    this.props.dispatch({ type: 'RECEIVE_STATUS', data: { id, group, text } });
    setTimeout(() => this.props.dispatch({ type: 'REMOVE_STATUS', data: id }), timeout);
  }

  clearMessageGroup(group) {
    this.props.dispatch({ type: 'CLEAR_STATUS_GROUP', data: group });
  }

  render() {
    return (
      <div className="StatusBar">
        {
          this.props.messages.map(message => <div key={message.id}>{message.text}</div>)
        }
      </div>
    );
  }
}

const mapStateToProps = state => ({
  messages: state.statusMessages
});

export default connect(mapStateToProps)(StatusBar);
