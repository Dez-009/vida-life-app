// Chat.js
import React, { useState } from 'react';
import MessageBubble from './MessageBubble';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (input.trim() === '') return;

    // Add user message to chat
    const newMessages = [...messages, { sender: 'user', text: input }];
    setMessages(newMessages);

    // Send message to backend
    const response = await fetch('http://127.0.0.1:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const data = await response.json();

    // Add AI response to chat
    setMessages([...newMessages, { sender: 'ai', text: data.response }]);
    setInput('');
  };

  return (
    <div className="chat-container">
      <div className="chat-window">
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <MessageBubble key={index} sender={msg.sender} text={msg.text} />
          ))}
        </div>
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chat;