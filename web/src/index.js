import { Router, Route, IndexRoute, Link, browserHistory } from 'react-router'
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux'
import { syncHistoryWithStore, routerReducer } from 'react-router-redux'

import configureStore from './redux/store';
import App from './routes/App';
import Main from './routes/Main';
import Game from './routes/Game';
import './index.css';

// IMPORT ALL ASSETS
import background from './assets/background.jpg';
import ninjaruto_font from './assets/njnaruto.ttf';

const store = configureStore();
const history = syncHistoryWithStore(browserHistory, store);

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <Route path="/" component={App}>
      <IndexRoute component={Main} />
      <Route path="game" component={Game} />
    </Route>
  </Router>
  </Provider>,
  document.getElementById('root')
);
