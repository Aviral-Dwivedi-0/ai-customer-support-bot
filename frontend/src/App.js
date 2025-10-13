/**
 * AI Customer Support Bot - Main React Application
 * ==================================================
 * 
 * This is the main component that manages the chat interface, state management,
 * and communication with the Flask backend API.
 * 
 * Features:
 *   - Real-time messaging with backend
 *   - Session-based conversation tracking
 *   - Typing indicators for better UX
 *   - Error handling and notifications
 *   - Auto-scroll to latest messages
 *   - Welcome message on load
 * 
 * Architecture:
 *   - Uses React Hooks (useState, useEffect, useRef) for state management
 *   - Axios for HTTP requests to Flask API
 *   - Component-based structure (ChatBubble, InputBox)
 * 
 * @author AI Customer Support Team
 * @date October 2025
 */

import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';
import ChatBubble from './components/ChatBubble';
import InputBox from './components/InputBox';

// Backend API base URL
const API_URL = 'http://localhost:5000';

function App() {
  // ========== STATE MANAGEMENT ==========
  
  /**
   * messages: Array of message objects
   * Each message has: {text, sender, timestamp, isError?}
   */
  const [messages, setMessages] = useState([]);
  
  /**
   * isTyping: Boolean indicating if bot is "typing"
   * Shows animated typing indicator to user
   */
  const [isTyping, setIsTyping] = useState(false);
  
  /**
   * sessionId: Unique identifier for this conversation session
   * Generated once on component mount using timestamp
   * Format: "session_<timestamp>"
   */
  const [sessionId] = useState(`session_${Date.now()}`);
  
  /**
   * error: String containing error message, or null if no error
   * Displayed in error banner at bottom of chat
   */
  const [error, setError] = useState(null);
  
  /**
   * messagesEndRef: Reference to bottom of message list
   * Used for auto-scrolling to newest messages
   */
  const messagesEndRef = useRef(null);

  // ========== HELPER FUNCTIONS ==========
  
  /**
   * Scroll to the bottom of the message list smoothly.
   * Called whenever new messages are added.
   */
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // ========== EFFECTS ==========
  
  /**
   * Effect: Auto-scroll when messages change
   * Triggers: Whenever messages array is updated
   */
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  /**
   * Effect: Display welcome message on component mount
   * Triggers: Once on initial render (empty dependency array)
   */
  useEffect(() => {
    setMessages([
      {
        text: "👋 Hello! I'm your AI customer support assistant. How can I help you today?",
        sender: 'bot',
        timestamp: new Date()
      }
    ]);
  }, []);

  // ========== MESSAGE HANDLING ==========
  
  /**
   * Send a message to the backend and handle the response.
   * 
   * Flow:
   *   1. Validate message is not empty
   *   2. Add user message to chat
   *   3. Show typing indicator
   *   4. Call backend API
   *   5. Add bot response to chat
   *   6. Handle any errors
   * 
   * @param {string} messageText - The user's message text
   */
  const sendMessage = async (messageText) => {
    // Validate input - don't send empty messages
    if (!messageText.trim()) return;

    // Create user message object
    const userMessage = {
      text: messageText,
      sender: 'user',
      timestamp: new Date()
    };
    
    // Add user message to chat immediately (optimistic UI update)
    setMessages(prev => [...prev, userMessage]);
    
    // Clear any previous errors
    setError(null);
    
    // Show typing indicator
    setIsTyping(true);

    try {
      // Call backend API with session ID and user query
      const response = await axios.post(`${API_URL}/chat`, {
        session_id: sessionId,
        query: messageText
      });

      // Create bot message object from API response
      const botMessage = {
        text: response.data.response,
        sender: 'bot',
        timestamp: new Date()
      };
      
      // Add bot response to chat
      setMessages(prev => [...prev, botMessage]);
      
    } catch (err) {
      // Log error for debugging
      console.error('Error sending message:', err);
      
      // Set user-friendly error message
      setError('Failed to send message. Please make sure the backend server is running.');
      
      // Add error message to chat UI
      const errorMessage = {
        text: "❌ Sorry, I'm having trouble connecting. Please try again later.",
        sender: 'bot',
        timestamp: new Date(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
      
    } finally {
      // Always hide typing indicator, whether success or error
      setIsTyping(false);
    }
  };

  // ========== RENDER ==========

  // ========== RENDER ==========

  return (
    <div className="App">
      <div className="chat-container">
        
        {/* ===== CHAT HEADER ===== */}
        <div className="chat-header">
          <div className="header-content">
            {/* Bot avatar icon */}
            <div className="bot-avatar">🤖</div>
            
            {/* Header text with title and online status */}
            <div className="header-text">
              <h1>AI Customer Support</h1>
              <p className="status">
                {/* Pulsing green dot to indicate online status */}
                <span className="status-dot"></span>
                Online
              </p>
            </div>
          </div>
        </div>

        {/* ===== CHAT MESSAGES AREA ===== */}
        <div className="chat-messages">
          {/* Render all messages using ChatBubble component */}
          {messages.map((message, index) => (
            <ChatBubble
              key={index}
              message={message.text}
              sender={message.sender}
              timestamp={message.timestamp}
              isError={message.isError}
            />
          ))}
          
          {/* Show typing indicator when bot is responding */}
          {isTyping && (
            <div className="typing-indicator">
              <div className="typing-bubble">
                <div className="typing-dots">
                  {/* Three animated dots */}
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          
          {/* Invisible element at bottom for auto-scrolling */}
          <div ref={messagesEndRef} />
        </div>

        {/* ===== ERROR BANNER ===== */}
        {/* Only shown when error state is not null */}
        {error && (
          <div className="error-banner">
            ⚠️ {error}
          </div>
        )}

        {/* ===== INPUT BOX ===== */}
        {/* Disabled during typing to prevent multiple simultaneous requests */}
        <InputBox onSendMessage={sendMessage} disabled={isTyping} />
      </div>
    </div>
  );
}

export default App;
