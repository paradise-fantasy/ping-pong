import { createStore, compose, combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';

import { configureSocket } from '../game-socket';
import { gameReducer } from './game';
import { playersReducer } from './players';
import { statusMessagesReducer } from './status-messages';

const reducer = combineReducers({
  game: gameReducer,
  players: playersReducer,
  statusMessages: statusMessagesReducer,
  routing: routerReducer
});


const configureStore = preloadedState => {
  const store = createStore(
    reducer,
    preloadedState,
    compose(
      window.devToolsExtension ? window.devToolsExtension() : f => f
    )
  );

  configureSocket(store.dispatch);

  return store;
}

export default configureStore;
