import React, { createContext, useState, useContext, useEffect, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [user, setUser] = useState(null);

  const fetchUserData = useCallback(async () => {
    try {
      const response = await axios.get('http://localhost:8000/users/me');
      setUser(response.data);
    } catch (error) {
      console.error('Failed to fetch user data:', error);
      logout();
    }
  }, []);

  useEffect(() => {
    if (token) {
      // Set default authorization header for all requests
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      
      // Fetch user data
      fetchUserData();
    } else {
      delete axios.defaults.headers.common['Authorization'];
    }
  }, [token, fetchUserData]);

  const login = (newToken) => {
    localStorage.setItem('token', newToken);
    setToken(newToken);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
    delete axios.defaults.headers.common['Authorization'];
  };

  return (
    <AuthContext.Provider value={{ token, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
