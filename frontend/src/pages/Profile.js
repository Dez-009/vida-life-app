import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';
import './Profile.css';

function Profile() {
  const { user } = useAuth();
  const [profile, setProfile] = useState({
    full_name: '',
    age: '',
    date_of_birth: '',
    address: '',
    phone: '',
    is_married: false,
    annual_income: '',
    number_of_children: '',
    sex: ''
  });
  const [isEditing, setIsEditing] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (user) {
      setProfile({
        full_name: user.full_name || '',
        age: user.age || '',
        date_of_birth: user.date_of_birth || '',
        address: user.address || '',
        phone: user.phone || '',
        is_married: user.is_married || false,
        annual_income: user.annual_income || '',
        number_of_children: user.number_of_children || '',
        sex: user.sex || ''
      });
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(
        'http://localhost:8000/users/me/profile',
        profile,
        {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        }
      );
      setMessage('Profile updated successfully!');
      setIsEditing(false);
    } catch (error) {
      setMessage('Failed to update profile. Please try again.');
    }
  };

  return (
    <div className="profile-container">
      <h1>Profile Information</h1>
      {message && <div className="message">{message}</div>}
      
      <form onSubmit={handleSubmit} className="profile-form">
        <div className="form-group">
          <label>Full Name:</label>
          <input
            type="text"
            name="full_name"
            value={profile.full_name}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>Age:</label>
          <input
            type="number"
            name="age"
            value={profile.age}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>Date of Birth:</label>
          <input
            type="date"
            name="date_of_birth"
            value={profile.date_of_birth}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>Address:</label>
          <textarea
            name="address"
            value={profile.address}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>Phone:</label>
          <input
            type="tel"
            name="phone"
            value={profile.phone}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>
            <input
              type="checkbox"
              name="is_married"
              checked={profile.is_married}
              onChange={handleChange}
              disabled={!isEditing}
            />
            Married
          </label>
        </div>

        <div className="form-group">
          <label>Annual Income:</label>
          <input
            type="number"
            name="annual_income"
            value={profile.annual_income}
            onChange={handleChange}
            disabled={!isEditing}
            step="0.01"
          />
        </div>

        <div className="form-group">
          <label>Number of Children:</label>
          <input
            type="number"
            name="number_of_children"
            value={profile.number_of_children}
            onChange={handleChange}
            disabled={!isEditing}
          />
        </div>

        <div className="form-group">
          <label>Sex:</label>
          <select
            name="sex"
            value={profile.sex}
            onChange={handleChange}
            disabled={!isEditing}
          >
            <option value="">Select...</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div className="button-group">
          {!isEditing ? (
            <button type="button" onClick={() => setIsEditing(true)} className="edit-button">
              Edit Profile
            </button>
          ) : (
            <>
              <button type="submit" className="save-button">Save Changes</button>
              <button 
                type="button" 
                onClick={() => setIsEditing(false)} 
                className="cancel-button"
              >
                Cancel
              </button>
            </>
          )}
        </div>
      </form>
    </div>
  );
}

export default Profile;
