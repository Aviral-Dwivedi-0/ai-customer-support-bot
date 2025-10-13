# 🤖 AI Customer Support Bot - Full Stack Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![React](https://img.shields.io/badge/React-18-61DAFB.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

**An intelligent AI-powered customer support chatbot built with Flask, React, and Google Gemini AI**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Tech Stack](#-tech-stack) • [Screenshots](#-screenshots)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This is a **production-ready full-stack AI customer support chatbot** that uses Google's Gemini AI to answer customer questions based on a FAQ knowledge base. The system features intelligent conversation management, automatic escalation to human agents, and a beautiful modern React interface.

### Key Highlights

✨ **AI-Powered** - Uses Google Gemini 2.5 Flash for intelligent responses  
💬 **Real-time Chat** - Beautiful, responsive chat interface  
🧠 **Context-Aware** - Maintains conversation history for better responses  
🚀 **Production Ready** - Comprehensive documentation and error handling  
📱 **Mobile Friendly** - Responsive design works on all devices  
🔒 **Secure** - API keys managed via environment variables

---

## ✨ Features

### Backend Features

- ✅ **Flask REST API** - Clean, well-documented API endpoints
- ✅ **Google Gemini AI Integration** - Advanced natural language processing
- ✅ **FAQ-Based Answering** - Answers only from verified knowledge base
- ✅ **Conversation Memory** - SQLite database for session persistence
- ✅ **Context-Aware Responses** - Uses conversation history for better answers
- ✅ **Smart Escalation** - Automatic handoff to human agents when needed
- ✅ **Conversation Summarization** - AI-generated summaries for agents
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Comprehensive Error Handling** - User-friendly error messages

### Frontend Features

- ✅ **Modern React UI** - Beautiful, intuitive chat interface
- ✅ **Real-time Messaging** - Instant communication with backend
- ✅ **Typing Indicators** - Visual feedback during bot responses
- ✅ **Message Timestamps** - All messages timestamped
- ✅ **Error Notifications** - Clear error handling and user feedback
- ✅ **Smooth Animations** - 60fps animations for better UX
- ✅ **Responsive Design** - Works perfectly on mobile and desktop
- ✅ **Session Management** - Unique session IDs for each conversation
- ✅ **Auto-scroll** - Automatically scrolls to new messages

---

## 🛠 Tech Stack

### Backend

- **Python 3.12** - Modern Python with type hints
- **Flask 3.0.0** - Lightweight web framework
- **SQLite 3** - Embedded database for conversations
- **Google Gemini AI** - Advanced language model
- **Flask-CORS** - Cross-origin resource sharing

### Frontend

- **React 18** - Modern UI library
- **Axios** - HTTP client for API calls
- **Custom CSS** - Beautiful animations and styling
- **JavaScript ES6+** - Modern JavaScript features

### Development Tools

- **Git** - Version control
- **VS Code** - Recommended editor
- **Python venv** - Virtual environment
- **npm** - Package management

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Node.js 16+
- npm 8+
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-customer-support-bot.git
   cd ai-customer-support-bot
   ```

2. **Backend Setup**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Create .env file with your API key
   echo GEMINI_API_KEY=your_api_key_here > .env
   ```

3. **Frontend Setup**

   ```bash
   cd frontend
   npm install
   ```

4. **Run the Application**

   **Option 1: Automated (Windows)**

   ```bash
   # From project root
   start-fullstack.bat
   ```

   **Option 2: Manual**

   ```bash
   # Terminal 1 - Backend
   venv\Scripts\activate
   python app.py

   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

5. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000
   - Health Check: http://localhost:5000/health

---

## 📁 Project Structure

```
ai-customer-support-bot/
├── backend/
│   ├── app.py                     # Flask application
│   ├── faqs.txt                   # FAQ knowledge base
│   ├── requirements.txt           # Python dependencies
│   ├── .env                       # Environment variables
│   └── conversations.db           # SQLite database
├── frontend/
│   ├── public/
│   │   └── index.html            # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBubble.js     # Message component
│   │   │   ├── ChatBubble.css    # Message styles
│   │   │   ├── InputBox.js       # Input component
│   │   │   └── InputBox.css      # Input styles
│   │   ├── App.js                # Main app component
│   │   ├── App.css               # Main styles
│   │   ├── index.js              # Entry point
│   │   └── index.css             # Global styles
│   └── package.json              # Node dependencies
├── docs/
│   ├── README.md                 # This file
│   ├── FULLSTACK_GUIDE.md        # Complete guide
│   ├── PROJECT_SUMMARY.md        # Technical summary
│   └── CODE_REVIEW_SUMMARY.md    # Code review report
├── .gitignore                    # Git ignore rules
├── .gitattributes                # Git attributes
└── LICENSE                       # MIT License
```

---

## 📚 Documentation

### Available Documentation

- **[README.md](README.md)** - Main documentation (you are here)
- **[FULLSTACK_GUIDE.md](FULLSTACK_GUIDE.md)** - Comprehensive setup and deployment guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Technical deep-dive and architecture
- **[QUICK_START.md](QUICK_START.md)** - 5-minute quick start guide
- **[CODE_REVIEW_SUMMARY.md](CODE_REVIEW_SUMMARY.md)** - Code quality review
- **[frontend/README.md](frontend/README.md)** - Frontend-specific documentation

---

## 🔌 API Endpoints

### `GET /health`

Health check endpoint to verify server status.

**Response:**

```json
{
  "status": "ok"
}
```

### `POST /chat`

Main chat endpoint for sending messages and receiving AI responses.

**Request:**

```json
{
  "session_id": "session_1234567890",
  "query": "What is your return policy?"
}
```

**Response:**

```json
{
  "response": "You can return products within 30 days of purchase with original packaging and receipt."
}
```

### `POST /escalate`

Get conversation summary for human agent escalation.

**Request:**

```json
{
  "session_id": "session_1234567890"
}
```

**Response:**

```json
{
  "summary": "Customer asked about return policy and shipping times..."
}
```

---

## 📸 Screenshots

### Chat Interface

![Chat Interface](docs/screenshots/chat-interface.png)
_Modern, responsive chat interface with typing indicators_

### Mobile View

![Mobile View](docs/screenshots/mobile-view.png)
_Fully responsive design works perfectly on mobile devices_

---

## 💻 Development

### Running Tests

```bash
# Backend tests
python test_api.py

# Quick diagnostic test
python quick_test.py

# Live demonstration
python demo.py
```

### Adding New FAQs

Edit `faqs.txt` and add your Q&A pairs:

```
Q: Your question here?
A: Your answer here.
```

### Customization

- **Theme Colors**: Edit `frontend/src/App.css`
- **Bot Behavior**: Modify prompts in `app.py`
- **FAQ Content**: Update `faqs.txt`
- **API URL**: Change `API_URL` in `frontend/src/App.js`

---

## 🧪 Testing

### Backend Tests (5 test scenarios)

✅ Health check endpoint  
✅ FAQ matching and response  
✅ Conversation context memory  
✅ Escalation workflow  
✅ Conversation summarization

**All tests passing: 5/5** ✅

### Manual Testing

1. Start both backend and frontend servers
2. Open http://localhost:3000
3. Test FAQ questions
4. Test follow-up questions (context)
5. Test non-FAQ questions (escalation)
6. Verify error handling

---

## 🚀 Deployment

### Backend Deployment

**Heroku:**

```bash
heroku create your-app-name
git push heroku main
```

**Railway:**

```bash
railway init
railway up
```

### Frontend Deployment

**Netlify:**

```bash
cd frontend
npm run build
netlify deploy --prod --dir=build
```

**Vercel:**

```bash
cd frontend
vercel --prod
```

See [FULLSTACK_GUIDE.md](FULLSTACK_GUIDE.md) for detailed deployment instructions.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **AI Development Team** - Initial work

---

## 🙏 Acknowledgments

- Google Gemini AI for the language model
- Flask community for the excellent web framework
- React team for the UI library
- All contributors who help improve this project

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ using React, Flask, and Google Gemini AI

</div>
