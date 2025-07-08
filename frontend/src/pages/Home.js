import React, { useEffect, useState } from 'react';
import './Home.css';

function Home() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <div className="home-page">
      <section className="hero-section">
        <h1 style={{ 
          opacity: isVisible ? 1 : 0, 
          transform: isVisible ? 'translateY(0)' : 'translateY(20px)',
          transition: 'all 1s ease-out'
        }}>
          Welcome to Vida Life Coach
        </h1>
        <p style={{ 
          opacity: isVisible ? 1 : 0, 
          transform: isVisible ? 'translateY(0)' : 'translateY(20px)',
          transition: 'all 1s ease-out 0.3s'
        }}>
          Your personal AI life coach to elevate, inspire, and transform your life journey.
        </p>
      </section>

      <div className="slogan">
        <p>"Apps shouldn't just function, but they should care for the user."</p>
      </div>

      <section className="feature-section">
        <div className="feature">
          <img 
            src="https://images.unsplash.com/photo-1525182008055-f88b95ff7980?auto=format&fit=crop&w=800&q=80" 
            alt="Real-time Chat"
            loading="lazy"
          />
          <div className="feature-text">
            <h2>Real-Time Conversations</h2>
            <p>Instantly chat with your AI coach and receive life-changing insights on demand.</p>
          </div>
        </div>

        <div className="divider"></div>

        <div className="feature reverse">
          <div className="feature-text">
            <h2>Goal Tracking</h2>
            <p>Set goals, track your growth, and watch your personal success story unfold.</p>
          </div>
          <img 
            src="https://images.unsplash.com/photo-1596495577886-d920f1fb7238?auto=format&fit=crop&w=800&q=80" 
            alt="Goal Tracking"
            loading="lazy"
          />
        </div>

        <div className="divider"></div>

        <div className="feature">
          <img 
            src="https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=800&q=80" 
            alt="Personalized Coaching"
            loading="lazy"
          />
          <div className="feature-text">
            <h2>Personalized Coaching</h2>
            <p>Receive tailored advice and motivational support unique to your life path.</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
