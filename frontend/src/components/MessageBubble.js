// MessageBubble.js
import React from 'react';

const MessageBubble = ({ sender, text }) => {
  return (
    <div className={`message-bubble ${sender}`}>
      {text}
    </div>
  );
};

export default MessageBubble;