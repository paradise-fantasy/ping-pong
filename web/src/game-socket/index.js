/**
 * Created by khrall on 26.01.2017.
 */
import SocketIO from 'socket.io-client';

const socket = SocketIO('http://localhost:5000')
socket.on('connect', () => {
  console.log('connected?')
});

socket.on('NEW_MATCH_STARTED', (match) => {
  console.log('new match started', match)
});


socket.on('MATCH_CANCELLED', (match) => {
  console.log('match cancelled', match)
});


socket.on('PLAYER_1_JOINED', (player) => {
  console.log('player 1 joined', player)
});

socket.on('GAME_OVER', (match) => {
  console.log('match over', match);
});



socket.on('PLAYER_1_SCORE_INC', (match) => {
  console.log('player 1 scored', match);
});

socket.on('PLAYER_2_SCORE_INC', (match) => {
  console.log('player 2 scored', match);
});

socket.on('PLAYER_1_SCORE_DEC', (match) => {
  console.log('player 1 reverted point', match);
});

socket.on('PLAYER_2_SCORE_DEC', (match) => {
  console.log('player 2 reverted point', match);
});


