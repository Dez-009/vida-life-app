import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Chat from './components/Chat';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
      <div className="navbar">
        <div className="navbar-link">Vida Life Coach</div>
        <div style={{ marginLeft: 'auto', display: 'flex' }}>
          <div className="navbar-link"><Link to="/" className="nav-link">New Chat</Link></div>
          <div className="navbar-link"><Link to="/profile" className="nav-link">Profile</Link></div>
          <div className="navbar-link"><Link to="/settings" className="nav-link">Settings</Link></div>
        </div>
      </div>

      <div className="hero-section">
        <h1>Elevate Your Life with Vida</h1>
        <p>Your personal AI life coach is here to guide you, motivate you, and help you conquer your goals. Experience real growth, one conversation at a time.</p>
        <div className="hero-cta">
          <button className="cta-button">Start Your Journey</button>
        </div>
      </div>

        <Routes>
          <Route path="/" element={<Chat />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
