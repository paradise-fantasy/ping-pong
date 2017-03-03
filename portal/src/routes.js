import React from 'react';
import { Router, Route } from 'react-router';

import App from './components/App';
import Register from './components/Register';
import NotFound from './components/NotFound';
import ComingSoon from './components/ComingSoon';

const Routes = (props) => (
    <Router {...props}>
        <Route path="/" component={App} />
        <Route path="/register" component={Register} />
        <Route path="/comingsoon" component={ComingSoon} />
        <Route path="*" component={NotFound} />
    </Router>
);

export default Routes;
