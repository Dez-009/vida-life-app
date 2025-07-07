import React from 'react';
import Chat from './components/Chat';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="navbar">
        <div className="navbar-link">Vida Life Coach</div>
        <div style={{ marginLeft: 'auto', display: 'flex' }}>
          <div className="navbar-link">New Chat</div>
          <div className="navbar-link">Profile</div>
          <div className="navbar-link">Settings</div>
        </div>
      </div>

      <div className="hero-section">
        <h1>Elevate Your Life with Vida</h1>
        <p>Your personal AI life coach is here to guide you, motivate you, and help you conquer your goals. Experience real growth, one conversation at a time.</p>
        <div className="hero-cta">
          <button className="cta-button">Start Your Journey</button>
        </div>
      </div>

      <div className="chat-container">
        <Chat />
      </div>
    </div>
  );
}

export default App;
