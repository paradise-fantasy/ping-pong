import { Router, Route, IndexRoute, Link, browserHistory } from 'react-router'
import React from 'react';
import ReactDOM from 'react-dom';
import App from './routes/App';
import Main from './routes/Main';
import Game from './routes/Game';
import './index.css';

// IMPORT ALL ASSETS
import background from './assets/background.jpg';
import ninjaruto_font from './assets/njnaruto.ttf';

ReactDOM.render(
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={Main} />
      <Route path="game" component={Game} />
    </Route>
  </Router>,
  document.getElementById('root')
);
