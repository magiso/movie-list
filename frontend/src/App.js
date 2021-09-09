import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import HomePage from './pages/HomePage';
import ToWatchPage from './pages/ToWatchPage';
import WatchedPage from './pages/WatchedPage';

// Route to different pages
function App() {
  document.title = 'My Movie List';
  return (
    <Router>
      <Switch>
        <Route path="/towatch" component={ToWatchPage} />
        <Route path="/watched" component={WatchedPage} />
        <Route path="/home" component={HomePage} />
      </Switch>
    </Router>
  );
}

export default App;
