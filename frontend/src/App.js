import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Chat from './components/Chat';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <div className="navbar">
          <div className="navbar-link"><Link to="/" className="nav-link">Home</Link></div>
          <div style={{ marginLeft: 'auto', display: 'flex' }}>
            <div className="navbar-link"><Link to="/chat" className="nav-link">New Chat</Link></div>
            <div className="navbar-link"><Link to="/profile" className="nav-link">Profile</Link></div>
            <div className="navbar-link"><Link to="/settings" className="nav-link">Settings</Link></div>
          </div>
        </div>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
