/**
 * InputBox Component
 * ==================
 *
 * Message input component with send button and keyboard shortcuts.
 *
 * Features:
 *   - Auto-expanding textarea for multi-line messages
 *   - Send button with icon
 *   - Keyboard shortcuts (Enter to send, Shift+Enter for new line)
 *   - Disabled state during message sending
 *   - Visual hint for keyboard shortcuts
 *
 * Props:
 *   @param {function} onSendMessage - Callback function when message is sent
 *   @param {boolean} disabled - Whether input is disabled (during bot response)
 *
 * @author AI Customer Support Team
 * @date October 2025
 */

import React, { useState } from "react";
import "./InputBox.css";

function InputBox({ onSendMessage, disabled }) {
  // ========== STATE MANAGEMENT ==========

  /**
   * input: Current value of the textarea
   * Controlled component pattern - React manages the input value
   */
  const [input, setInput] = useState("");

  // ========== EVENT HANDLERS ==========

  /**
   * Handle form submission.
   *
   * Triggered by:
   *   - Clicking send button
   *   - Pressing Enter key (via handleKeyPress)
   *
   * @param {Event} e - Form submit event
   */
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent page reload

    // Only send if input has content and not disabled
    if (input.trim() && !disabled) {
      onSendMessage(input); // Call parent callback with message
      setInput(""); // Clear input field
    }
  };

  /**
   * Handle keyboard shortcuts in textarea.
   *
   * Shortcuts:
   *   - Enter: Send message (if not holding Shift)
   *   - Shift+Enter: Insert new line (default textarea behavior)
   *
   * @param {KeyboardEvent} e - Keyboard event
   */
  const handleKeyPress = (e) => {
    // Check for Enter key WITHOUT Shift
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault(); // Prevent default new line insertion
      handleSubmit(e); // Send message instead
    }
    // If Shift+Enter, do nothing (allow default new line)
  };

  // ========== RENDER ==========

  return (
    <div className="input-box-container">
      {/* Form wrapper for submit functionality */}
      <form onSubmit={handleSubmit} className="input-form">
        {/* Message input textarea */}
        <textarea
          className="message-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
          disabled={disabled}
          rows="1" // Start with single row, expands automatically via CSS
        />

        {/* Send button with SVG icon */}
        <button
          type="submit"
          className="send-button"
          disabled={disabled || !input.trim()} // Disable if sending or empty input
        >
          {/* Paper plane icon (send symbol) */}
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </form>

      {/* Hint text for keyboard shortcuts */}
      <div className="input-hint">
        Press Enter to send • Shift+Enter for new line
      </div>
    </div>
  );
}

export default InputBox;
