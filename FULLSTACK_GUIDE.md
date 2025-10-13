# 🚀 AI Customer Support Bot - Full Stack Guide

Complete documentation for the full-stack AI Customer Support Bot with React frontend and Flask backend.

---

## 📦 Project Overview

### Architecture
```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   React Frontend│ ◄─────► │  Flask Backend   │ ◄─────► │  Gemini API     │
│   (Port 3000)   │  HTTP   │   (Port 5000)    │  HTTPS  │  (Google AI)    │
└─────────────────┘         └──────────────────┘         └─────────────────┘
                                      │
                                      ▼
                            ┌──────────────────┐
                            │  SQLite Database │
                            │  conversations.db │
                            └──────────────────┘
```

### Technology Stack

**Frontend:**
- ⚛️ React 18
- 📡 Axios for HTTP requests
- 🎨 Custom CSS with animations
- 📱 Responsive design

**Backend:**
- 🐍 Python 3.12
- 🌐 Flask 3.0.0
- 🗄️ SQLite for session storage
- 🤖 Google Gemini 2.5 Flash AI
- 🔐 flask-cors for API access

---

## 🚀 Quick Start (Full Stack)

### Option 1: Automated Setup (Windows)

```bash
# Run the automated startup script
start-fullstack.bat
```

This will:
1. Start Flask backend on port 5000
2. Start React frontend on port 3000
3. Open both in separate windows

### Option 2: Manual Setup

#### Terminal 1 - Backend
```bash
# Activate virtual environment
venv\Scripts\activate

# Start Flask server
python app.py
```

#### Terminal 2 - Frontend
```bash
# Navigate to frontend
cd frontend

# Install dependencies (first time only)
npm install

# Start development server
npm start
```

---

## 📋 Detailed Setup Instructions

### Prerequisites
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ and npm installed
- ✅ Gemini API key (in `.env` file)
- ✅ Internet connection

### Backend Setup

1. **Create virtual environment (if not exists):**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create `.env` file with:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Start the backend:**
   ```bash
   python app.py
   ```

   ✅ Backend running at: `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

   This installs:
   - react
   - react-dom
   - react-scripts
   - axios

3. **Start the frontend:**
   ```bash
   npm start
   ```

   ✅ Frontend running at: `http://localhost:3000`

---

## 🎯 Features

### Frontend Features
- 💬 Beautiful chat interface
- ⌨️ Real-time typing indicators
- 🎨 Smooth animations
- 📱 Mobile responsive
- ⚡ Instant message updates
- 🚨 Error handling with notifications
- 🕐 Message timestamps

### Backend Features
- 🤖 AI-powered responses (Gemini 2.5 Flash)
- 📝 FAQ-based answering
- 🧠 Conversation memory
- 🚀 Smart escalation to humans
- 📊 Session management
- 🔄 Conversation summarization
- 🛡️ Error handling
- 🔐 CORS enabled for frontend

---

## 🔧 Configuration

### Backend Configuration

**Port:** 5000 (default)
To change, edit `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=YOUR_PORT)
```

**CORS:** Enabled for all origins by default
To restrict, edit `app.py`:
```python
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
```

### Frontend Configuration

**Backend API URL:** `http://localhost:5000` (default)
To change, edit `frontend/src/App.js`:
```javascript
const API_URL = 'http://your-backend-url';
```

**Port:** 3000 (default)
To change:
```bash
PORT=3001 npm start
```

---

## 📡 API Endpoints

### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "ok"
}
```

### POST /chat
Send message to chatbot

**Request:**
```json
{
  "session_id": "unique_session_id",
  "query": "What is your return policy?"
}
```

**Response:**
```json
{
  "response": "You can return products within 30 days..."
}
```

### POST /escalate
Get conversation summary

**Request:**
```json
{
  "session_id": "unique_session_id"
}
```

**Response:**
```json
{
  "summary": "Customer asked about return policy..."
}
```

---

## 🧪 Testing

### Backend Testing
```bash
# Run comprehensive API tests
python test_api.py

# Run quick diagnostic test
python quick_test.py

# Run live demonstration
python demo.py
```

### Frontend Testing
```bash
cd frontend
npm test
```

### Full Stack Testing
1. Start both servers
2. Open `http://localhost:3000`
3. Test conversation flow:
   - Ask FAQ questions
   - Test follow-up questions (context)
   - Test escalation (unknown questions)

---

## 📁 Project Structure

```
ai-customer-support-bot/
├── frontend/                   # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBubble.js
│   │   │   ├── ChatBubble.css
│   │   │   ├── InputBox.js
│   │   │   └── InputBox.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── README.md
├── venv/                       # Python virtual environment
├── app.py                      # Flask backend
├── faqs.txt                    # FAQ knowledge base
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── conversations.db            # SQLite database
├── test_api.py                # API tests
├── README.md                   # Main documentation
├── start-fullstack.bat        # Startup script (Windows)
└── setup-frontend.bat         # Frontend setup script
```

---

## 🎨 Customization

### Change Theme Colors

Edit `frontend/src/App.css`:
```css
/* Primary gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to your colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

### Add More FAQs

Edit `faqs.txt`:
```
Q: Your new question?
A: Your new answer.
```

Restart backend to load new FAQs.

### Modify Bot Personality

Edit `app.py` - `construct_prompt()` function:
```python
prompt = f"""You are a [YOUR PERSONALITY] customer support assistant..."""
```

---

## 🚀 Deployment

### Frontend Deployment

#### Build for Production
```bash
cd frontend
npm run build
```

#### Deploy to Netlify
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd frontend
netlify deploy --prod --dir=build
```

#### Deploy to Vercel
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd frontend
vercel --prod
```

### Backend Deployment

#### Deploy to Heroku
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Deploy to Railway
1. Connect GitHub repository
2. Select project
3. Add environment variables
4. Deploy automatically

### Full Stack Deployment
1. Deploy backend first
2. Get backend URL
3. Update frontend `API_URL`
4. Build and deploy frontend

---

## 🐛 Troubleshooting

### Backend Issues

**Issue:** Port 5000 already in use
**Solution:**
```bash
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

**Issue:** Gemini API key not found
**Solution:**
- Check `.env` file exists
- Verify API key is correct
- Restart backend after adding key

### Frontend Issues

**Issue:** Cannot connect to backend
**Solution:**
- Ensure backend is running on port 5000
- Check CORS is enabled in `app.py`
- Verify `API_URL` in `App.js`

**Issue:** npm install fails
**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### CORS Issues

**Problem:** Access blocked by CORS policy
**Solution:** Ensure flask-cors is installed:
```bash
pip install flask-cors
```

And enabled in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

## 📊 Performance

### Backend
- Average response time: ~1-2 seconds
- Handles concurrent requests
- Database operations are fast (SQLite)

### Frontend
- Lightweight bundle size
- Fast initial load
- Smooth animations (60fps)
- Optimized re-renders

---

## 🔒 Security Best Practices

### Backend
- ✅ API keys in environment variables
- ✅ Input validation on all endpoints
- ✅ SQL injection prevention (parameterized queries)
- ✅ Error messages don't leak sensitive info
- ⚠️ Add rate limiting for production
- ⚠️ Use HTTPS in production

### Frontend
- ✅ No sensitive data in frontend code
- ✅ Environment-based configuration
- ✅ XSS protection (React escapes by default)
- ⚠️ Add authentication for production
- ⚠️ Implement rate limiting

---

## 🎓 Development Tips

### Backend Development
```bash
# Auto-reload is enabled in debug mode
# Just save files and Flask will reload

# Check logs in terminal for errors
# Use print() or logging for debugging
```

### Frontend Development
```bash
# Hot reload is automatic
# Just save files and browser refreshes

# Open React DevTools for debugging
# Use console.log() for quick debugging
```

---

## 📈 Future Enhancements

### Frontend
- [ ] User authentication
- [ ] Message persistence
- [ ] File uploads
- [ ] Voice messages
- [ ] Dark mode
- [ ] Emoji picker
- [ ] Message search
- [ ] Export conversation

### Backend
- [ ] Rate limiting
- [ ] User authentication
- [ ] Logging system
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Caching layer
- [ ] Webhook support
- [ ] Admin panel

### Infrastructure
- [ ] Docker containers
- [ ] CI/CD pipeline
- [ ] Load balancing
- [ ] Database backups
- [ ] Monitoring (Prometheus)
- [ ] Error tracking (Sentry)

---

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Axios Documentation](https://axios-http.com/)

---

## 📝 License

MIT License - Feel free to use and modify

---

## 👨‍💻 Support

For issues or questions:
1. Check troubleshooting section
2. Review documentation files
3. Check terminal logs for errors

---

**Built with ❤️ using React, Flask, and Google Gemini AI**

Last Updated: October 14, 2025
