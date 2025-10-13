/**
 * ChatBubble Component
 * ====================
 *
 * Displays an individual chat message with styling based on sender type.
 *
 * Features:
 *   - Different styling for user vs bot messages
 *   - Timestamp display in readable format
 *   - Error state styling for error messages
 *   - Smooth fade-in animation
 *
 * Props:
 *   @param {string} message - The message text to display
 *   @param {string} sender - Message sender type ('user' or 'bot')
 *   @param {Date} timestamp - Message timestamp
 *   @param {boolean} isError - Whether this is an error message (optional)
 *
 * @author AI Customer Support Team
 * @date October 2025
 */

import React from "react";
import "./ChatBubble.css";

function ChatBubble({ message, sender, timestamp, isError }) {
  /**
   * Format timestamp into readable time string.
   *
   * Converts Date object to 12-hour format with AM/PM.
   * Example: 2:45 PM
   *
   * @param {Date} date - The timestamp to format
   * @returns {string} Formatted time string
   */
  const formatTime = (date) => {
    return new Date(date).toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    // Container with alignment class based on sender
    // user messages align right, bot messages align left
    <div className={`chat-bubble-container ${sender}`}>
      {/* Message bubble with sender-specific styling */}
      <div className={`chat-bubble ${sender} ${isError ? "error" : ""}`}>
        {/* Main message text */}
        <div className="message-text">{message}</div>

        {/* Timestamp in small text */}
        <div className="message-time">{formatTime(timestamp)}</div>
      </div>
    </div>
  );
}

export default ChatBubble;
