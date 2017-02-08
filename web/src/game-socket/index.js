/**
 * Created by khrall on 26.01.2017.
 */
import SocketIO from 'socket.io-client';

const SOCKET_HOST = process.env.REACT_APP_SOCKET_HOST || 'localhost';
const SOCKET_PORT = process.env.REACT_APP_SOCKET_PORT || '5000';
const socket = SocketIO(`http://${SOCKET_HOST}:${SOCKET_PORT}`);

socket.on('connect', () => {
  console.log('WebSocket connected')
});

socket.on('GAME_EVENT', msg => console.log(msg));
socket.on('MESSAGE', msg => console.log(msg));

const configureSocket = dispatch => {
  socket.on('GAME_EVENT', action => dispatch(action));
}

export {
  socket,
  configureSocket
}
