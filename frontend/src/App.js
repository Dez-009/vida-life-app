import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, useNavigate, Link } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Home from './pages/Home';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Chat from './components/Chat';
import './App.css';

// Protected Route wrapper component
const ProtectedRoute = ({ children }) => {
  const { token } = useAuth();
  
  if (!token) {
    return <Navigate to="/login" />;
  }
  
  return children;
};

function Navigation({ onLogout }) {
  return (
    <nav className="nav">
      <div className="nav-content">
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/profile">Profile</Link>
          <Link to="/chat">Chat</Link>
          <Link to="/settings">Settings</Link>
          <button className="logout-button" onClick={onLogout}>Logout</button>
        </div>
      </div>
    </nav>
  );
}

function AppContent() {
  const { token, login, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="app">
      {token ? (
        <>
          <Navigation onLogout={handleLogout} />
          <div className="container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route 
                path="/profile" 
                element={
                  <ProtectedRoute>
                    <Profile />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/settings" 
                element={
                  <ProtectedRoute>
                    <Settings />
                  </ProtectedRoute>
                } 
              />
              <Route 
                path="/chat" 
                element={
                  <ProtectedRoute>
                    <Chat />
                  </ProtectedRoute>
                } 
              />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </div>
        </>
      ) : (
        <Routes>
          <Route path="/login" element={<Login onLogin={login} />} />
          <Route path="/register" element={<Register onRegisterSuccess={() => navigate('/login')} />} />
          <Route path="*" element={<Navigate to="/login" />} />
        </Routes>
      )}
    </div>
  );
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </Router>
  );
}

export default App;
