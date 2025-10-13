# AI Customer Support Bot - Frontend

Beautiful, modern React frontend for the AI Customer Support Bot.

## Features

- 🎨 Modern, responsive chat interface
- 💬 Real-time messaging with typing indicators
- 🎯 Clean, intuitive UX
- 📱 Mobile-friendly design
- ⚡ Fast and lightweight

## Setup Instructions

### Prerequisites

- Node.js 16+ and npm installed
- Backend API running on `http://localhost:5000`

### Installation

1. **Navigate to frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

The app will open at `http://localhost:3000`

## Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── components/
│   │   ├── ChatBubble.js   # Message bubble component
│   │   ├── ChatBubble.css
│   │   ├── InputBox.js     # Message input component
│   │   └── InputBox.css
│   ├── App.js              # Main app component
│   ├── App.css             # Main styles
│   ├── index.js            # Entry point
│   └── index.css           # Global styles
└── package.json            # Dependencies
```

## Components

### App.js

Main application component that:

- Manages conversation state
- Handles API calls to backend
- Displays chat messages
- Shows typing indicators
- Handles errors

### ChatBubble

Renders individual messages with:

- User/bot styling
- Timestamps
- Smooth animations
- Error states

### InputBox

Message input component with:

- Text area for typing
- Send button
- Keyboard shortcuts (Enter to send)
- Disabled state during sending

## Configuration

### Backend API URL

The frontend connects to the backend at `http://localhost:5000` by default.

To change this, edit `src/App.js`:

```javascript
const API_URL = "http://your-backend-url";
```

## Features Implemented

### Real-time Chat

- Send messages to AI bot
- Receive intelligent responses
- View conversation history

### Typing Indicator

- Shows animated dots while bot is thinking
- Improves user experience

### Error Handling

- Connection error messages
- Failed request notifications
- Graceful degradation

### Responsive Design

- Works on desktop, tablet, and mobile
- Touch-friendly interface
- Adaptive layout

## Styling

The app uses a beautiful gradient purple theme with:

- Smooth animations
- Modern shadows and effects
- Clean typography
- Accessible colors

### Color Scheme

- Primary: #667eea → #764ba2 (Purple gradient)
- Background: #f7fafc (Light gray)
- Text: #333 (Dark gray)
- Success: #4ade80 (Green)
- Error: #991b1b (Red)

## API Integration

The frontend communicates with the Flask backend using Axios:

### POST /chat

```javascript
{
  "session_id": "unique_id",
  "query": "user message"
}
```

Response:

```javascript
{
  "response": "bot response"
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development

### Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

### Hot Reload

The dev server supports hot module replacement. Changes are reflected instantly without losing state.

## Production Build

To create a production build:

```bash
npm run build
```

This creates an optimized build in the `build/` directory.

## Deployment

### Deploy with Backend

1. Build the frontend: `npm run build`
2. Serve the `build/` directory with your Flask app
3. Configure Flask to serve static files

### Deploy Separately

1. Build the frontend
2. Deploy to:

   - Netlify
   - Vercel
   - GitHub Pages
   - Any static hosting service

3. Update the `API_URL` to point to your deployed backend

## Troubleshooting

### Backend Connection Error

**Problem:** "Failed to send message"
**Solution:** Ensure Flask backend is running on port 5000

### CORS Error

**Problem:** Cross-origin request blocked
**Solution:** Backend has flask-cors installed and configured

### Port Already in Use

**Problem:** Port 3000 is already in use
**Solution:** Kill the process or use a different port:

```bash
PORT=3001 npm start
```

## Future Enhancements

- [ ] Message history persistence
- [ ] User authentication
- [ ] File upload support
- [ ] Voice messages
- [ ] Dark mode
- [ ] Emoji picker
- [ ] Message search
- [ ] Export conversation

## License

MIT License

## Author

Built with ❤️ using React and modern web technologies
