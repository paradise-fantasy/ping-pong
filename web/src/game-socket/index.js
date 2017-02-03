/**
 * Created by khrall on 26.01.2017.
 */
import SocketIO from 'socket.io-client';

const socket = SocketIO('http://localhost:5000')

socket.on('connect', () => {
  console.log('WebSocket connected')
});

const configureSocket = dispatch => {
  socket.on('GAME_EVENT', action => dispatch(action));
}

export {
  socket,
  configureSocket
}
