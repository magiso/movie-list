import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

//import HomePage from './pages/HomePage';
import ToWatchPage from './pages/ToWatchPage';

// Route to different pages
function App() {
  document.title = 'My Movie List';
  return (
    <Router>
      <Switch>
        <Route path="/towatch" component={ToWatchPage}>
        </Route>;
        <Route path="/watched">
          <p> Movies i've watched! </p>
        <Route path="/">
          <p> Some Text! </p>
        </Route>;
        </Route>;
      </Switch>
    </Router>
  );
}

export default App;
