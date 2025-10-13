# 📁 Project Structure - AI Customer Support Bot

## Complete Directory Tree

```
ai-customer-support-bot/
│
├── 📂 backend/                          # Backend Application (Python/Flask)
│   │
│   ├── 📂 app/                          # Main Application Package
│   │   ├── __init__.py                  # Package initialization
│   │   └── main.py                      # Flask app, API routes, Gemini integration
│   │
│   ├── 📂 config/                       # Configuration Files
│   │   └── faqs.txt                     # FAQ knowledge base for AI
│   │
│   ├── 📂 data/                         # Data Storage
│   │   └── conversations.db             # SQLite database (conversation history)
│   │
│   ├── 📂 scripts/                      # Utility Scripts
│   │   ├── __init__.py                  # Package initialization
│   │   ├── demo.py                      # Live demo with 5 scenarios
│   │   ├── diagnose.py                  # System diagnostic tool
│   │   └── list_models.py               # List available Gemini models
│   │
│   ├── 📂 tests/                        # Test Suite
│   │   ├── __init__.py                  # Package initialization
│   │   ├── test_api.py                  # Full API test suite (5 tests)
│   │   └── quick_test.py                # Quick smoke tests (2 scenarios)
│   │
│   ├── __init__.py                      # Backend package initialization
│   ├── .env.example                     # Environment variables template
│   ├── requirements.txt                 # Python dependencies
│   ├── README.md                        # Backend documentation
│   └── run.py                           # Server startup script ⚡
│
├── 📂 frontend/                         # Frontend Application (React)
│   │
│   ├── 📂 public/                       # Static Assets
│   │   └── index.html                   # HTML template
│   │
│   ├── 📂 src/                          # React Source Code
│   │   │
│   │   ├── 📂 components/               # React Components
│   │   │   ├── ChatBubble.js            # Message bubble component
│   │   │   ├── ChatBubble.css           # Bubble styling
│   │   │   ├── InputBox.js              # User input component
│   │   │   └── InputBox.css             # Input styling
│   │   │
│   │   ├── App.js                       # Main React component
│   │   ├── App.css                      # Main app styles
│   │   ├── index.js                     # React entry point
│   │   └── index.css                    # Global styles
│   │
│   ├── package.json                     # NPM dependencies
│   ├── package-lock.json                # Dependency lock file
│   └── README.md                        # Frontend documentation
│
├── 📂 docs/                             # Project Documentation
│   ├── CHECKLIST.md                     # Project completion checklist
│   ├── CODE_REVIEW_BANNER.txt           # Code review banner
│   ├── CODE_REVIEW_CHECKLIST.md         # Code review checklist
│   ├── CODE_REVIEW_EXECUTIVE_SUMMARY.md # Code review executive summary
│   ├── CODE_REVIEW_SUMMARY.md           # Detailed code review
│   ├── FULLSTACK_COMPLETE.txt           # Completion banner
│   ├── FULLSTACK_GUIDE.md               # Full stack development guide
│   ├── Implementation_Plan.md           # Original implementation plan
│   ├── Product_Documentation.md         # Product specifications
│   ├── PROJECT_BANNER.txt               # Project banner
│   ├── PROJECT_SUMMARY.md               # Project summary
│   └── REPO_README.md                   # GitHub repository README
│
├── 📂 venv/                             # Python Virtual Environment
│   └── [Python environment files]       # (excluded from git)
│
├── 📄 .env                              # Environment Variables (API keys)
├── 📄 .env.example                      # Environment template
├── 📄 .gitignore                        # Git ignore rules
├── 📄 .gitattributes                    # Git attributes for line endings
├── 📄 README.md                         # Main project README ⭐
├── 📄 QUICK_START.md                    # Quick start guide
├── 📄 package-lock.json                 # Root package lock
├── 📄 setup-frontend.bat                # Frontend setup script (Windows)
└── 📄 start-fullstack.bat               # Full stack startup (Windows) 🚀

```

## 🎯 Key Files

### Backend Entry Points
- **`backend/run.py`** - Start the Flask server
- **`backend/app/main.py`** - Main application code (API endpoints)
- **`backend/config/faqs.txt`** - Edit to update chatbot knowledge

### Frontend Entry Points
- **`frontend/src/App.js`** - Main React component
- **`frontend/src/index.js`** - React entry point
- **`frontend/package.json`** - NPM dependencies

### Configuration
- **`.env`** - Store your GEMINI_API_KEY here (not in git)
- **`backend/requirements.txt`** - Python dependencies
- **`frontend/package.json`** - JavaScript dependencies

### Testing & Utilities
- **`backend/tests/test_api.py`** - Full API test suite
- **`backend/scripts/demo.py`** - Live demonstration
- **`backend/scripts/diagnose.py`** - Diagnostic tool

### Documentation
- **`README.md`** - Main project documentation
- **`QUICK_START.md`** - Quick reference guide
- **`docs/`** - Detailed documentation and guides

## 🚀 Running the Application

### Option 1: Automated (Windows)
```bash
start-fullstack.bat
```

### Option 2: Manual

**Backend:**
```bash
cd backend
python run.py
```

**Frontend:**
```bash
cd frontend
npm start
```

## 📊 Statistics

- **Total Lines of Code**: ~25,000+
- **Backend Files**: 12 Python files
- **Frontend Files**: 8 JavaScript/CSS files
- **Documentation**: 15+ markdown files
- **Tests**: 7 comprehensive test scenarios

## 🔧 Maintenance

### Adding New FAQs
Edit: `backend/config/faqs.txt`

### Updating Styles
Edit: `frontend/src/App.css` or component-specific CSS

### Adding API Endpoints
Edit: `backend/app/main.py`

### Adding Tests
Add to: `backend/tests/`

## 📝 Notes

- **Virtual Environment**: All Python dependencies are in `venv/`
- **Node Modules**: Frontend dependencies in `frontend/node_modules/`
- **Database**: SQLite database in `backend/data/conversations.db`
- **Environment Variables**: Store sensitive keys in `.env` (root and backend/)

## 🌟 Clean Architecture

This structure follows best practices:
- ✅ Separation of concerns (frontend/backend)
- ✅ Modular code organization
- ✅ Clear folder hierarchy
- ✅ Comprehensive documentation
- ✅ Easy to navigate and maintain
- ✅ Ready for production deployment
