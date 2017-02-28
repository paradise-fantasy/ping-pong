import React from 'react';
import { Router, Route } from 'react-router';

import App from './components/App';
import Register from './components/Register';
import NotFound from './components/NotFound';

const Routes = (props) => (
    <Router {...props}>
        <Route path="/" component={App} />
        <Route path="/register" component={Register} />
        <Route path="*" component={NotFound} />
    </Router>
);

export default Routes;
