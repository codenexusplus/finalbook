import React, { useState } from 'react';
import Layout from '@theme-original/Layout';
import { Chatbot } from '@site/src/components/Chatbot';

export default function LayoutWrapper(props) {
  const [isChatbotVisible, setChatbotVisible] = useState(false);

  const toggleChatbot = () => {
    setChatbotVisible(!isChatbotVisible);
  };

  return (
    <>
      <Layout {...props} />
      <div style={{ position: 'fixed', bottom: '20px', right: '20px', zIndex: 1000 }}>
        <button
          onClick={toggleChatbot}
          style={{
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '50%',
            width: '60px',
            height: '60px',
            fontSize: '24px',
            cursor: 'pointer',
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.2)',
          }}
        >
          🤖
        </button>
      </div>
      {isChatbotVisible && (
        <div style={{ position: 'fixed', bottom: '90px', right: '20px', zIndex: 1000 }}>
          <Chatbot />
        </div>
      )}
    </>
  );
}
