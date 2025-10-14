# 🚀 Vercel Deployment Guide - AI Customer Support Bot

## Overview

This guide will help you deploy your full-stack AI Customer Support Bot to Vercel.

**Architecture:**

- **Backend (Flask):** Deployed as Vercel Serverless Function
- **Frontend (React):** Deployed as Static Site on Vercel

---

## 📋 Prerequisites

1. ✅ GitHub account (you already have: Aviral-Dwivedi-0)
2. ✅ Vercel account (sign up at https://vercel.com with GitHub)
3. ✅ Your code pushed to GitHub (already done)
4. ✅ Gemini API Key

---

## 🎯 Deployment Strategy

We'll deploy in two parts:

1. **Backend API** → Vercel Serverless (separate project)
2. **Frontend** → Vercel Static Site (separate project)

---

## 📦 Part 1: Deploy Backend (Flask API)

### Step 1: Prepare Backend for Deployment

The following files have been created for you:

- ✅ `backend/vercel.json` - Vercel configuration
- ✅ `backend/index.py` - Vercel entry point

### Step 2: Create Separate Backend Repository (Option A - Recommended)

**Option A: Create a new repository for backend**

```bash
# Navigate to backend directory
cd backend

# Initialize git (if needed)
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: Flask backend for Vercel"

# Create new repo on GitHub: ai-customer-support-backend
# Then push
git remote add origin https://github.com/Aviral-Dwivedi-0/ai-customer-support-backend.git
git branch -M main
git push -u origin main
```

**Option B: Use subdirectory from existing repo (Alternative)**

You can also deploy the backend folder directly from your existing repo.

### Step 3: Deploy Backend to Vercel

1. **Go to Vercel Dashboard:**

   - Visit: https://vercel.com/new
   - Sign in with GitHub

2. **Import Project:**

   - Click "Add New..." → "Project"
   - Select your repository (ai-customer-support-backend or ai-customer-support-bot)
   - If using existing repo, set "Root Directory" to `backend`

3. **Configure Project:**

   ```
   Framework Preset: Other
   Root Directory: backend (if using monorepo)
   Build Command: (leave empty)
   Output Directory: (leave empty)
   Install Command: pip install -r requirements.txt
   ```

4. **Add Environment Variables:**

   - Click "Environment Variables"
   - Add: `GEMINI_API_KEY` = `your-gemini-api-key-here`
   - Add: `FLASK_ENV` = `production`

5. **Deploy:**
   - Click "Deploy"
   - Wait for deployment (2-3 minutes)
   - You'll get a URL like: `https://your-backend.vercel.app`

### Step 4: Test Backend API

Once deployed, test your backend:

```bash
# Test health check
curl https://your-backend.vercel.app/

# Test chat endpoint
curl -X POST https://your-backend.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What payment methods do you accept?"}'
```

---

## 🎨 Part 2: Deploy Frontend (React)

### Step 1: Update API URL in Frontend

Before deploying frontend, update the backend URL:

**File: `frontend/src/App.js`**

Find this line (around line 10-15):

```javascript
const API_URL = "http://localhost:5000";
```

Replace with your Vercel backend URL:

```javascript
const API_URL =
  process.env.REACT_APP_API_URL || "https://your-backend.vercel.app";
```

### Step 2: Add Environment Variable File

Create `frontend/.env.production`:

```
REACT_APP_API_URL=https://your-backend.vercel.app
```

### Step 3: Deploy Frontend to Vercel

1. **Go to Vercel Dashboard:**

   - Visit: https://vercel.com/new
   - Click "Add New..." → "Project"

2. **Import Project:**

   - Select your repository (ai-customer-support-bot)
   - Set "Root Directory" to `frontend`

3. **Configure Project:**

   ```
   Framework Preset: Create React App
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: build
   Install Command: npm install
   ```

4. **Add Environment Variables:**

   - Click "Environment Variables"
   - Add: `REACT_APP_API_URL` = `https://your-backend.vercel.app`

5. **Deploy:**
   - Click "Deploy"
   - Wait for deployment (2-3 minutes)
   - You'll get a URL like: `https://your-frontend.vercel.app`

---

## 🔧 Alternative: Deploy Both from Monorepo

If you want to deploy both from the same repository:

### Backend Deployment (Project 1)

- Repository: ai-customer-support-bot
- Root Directory: `backend`
- Framework: Other
- Environment Variables: `GEMINI_API_KEY`

### Frontend Deployment (Project 2)

- Repository: ai-customer-support-bot
- Root Directory: `frontend`
- Framework: Create React App
- Environment Variables: `REACT_APP_API_URL`

---

## 🌐 Update CORS Settings

After deploying frontend, update backend CORS settings:

**File: `backend/app/main.py`**

Update the CORS configuration to include your Vercel frontend URL:

```python
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",
            "https://your-frontend.vercel.app",
            "https://*.vercel.app"  # Allow all Vercel preview deployments
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
```

After updating, commit and push changes to redeploy.

---

## ✅ Post-Deployment Checklist

- [ ] Backend deployed and accessible
- [ ] Backend API endpoints working (test with curl/Postman)
- [ ] Frontend deployed and accessible
- [ ] Frontend can connect to backend API
- [ ] Environment variables set correctly
- [ ] CORS configured properly
- [ ] Chat functionality working end-to-end
- [ ] FAQ responses accurate

---

## 🎯 Quick Command Reference

### Deploy Backend (if using separate repo)

```bash
cd backend
git init
git add .
git commit -m "Deploy backend to Vercel"
git remote add origin https://github.com/Aviral-Dwivedi-0/ai-customer-support-backend.git
git push -u origin main
```

### Update Frontend API URL

```bash
cd frontend
# Edit src/App.js - update API_URL
# Create .env.production with REACT_APP_API_URL
git add .
git commit -m "Configure for Vercel deployment"
git push
```

---

## 🔍 Troubleshooting

### Backend Issues

**Error: Module not found**

- Check `requirements.txt` includes all dependencies
- Redeploy after updating requirements.txt

**Error: 500 Internal Server Error**

- Check Vercel logs: Dashboard → Project → Functions
- Verify `GEMINI_API_KEY` is set correctly
- Check that `index.py` is in the backend directory

**Error: CORS issues**

- Update CORS origins in `app/main.py`
- Include your frontend Vercel URL
- Redeploy backend after changes

### Frontend Issues

**Error: Network request failed**

- Check `REACT_APP_API_URL` is set correctly
- Verify backend is deployed and accessible
- Check browser console for CORS errors

**Error: Build failed**

- Check `package.json` dependencies
- Run `npm install` locally to verify
- Check Vercel build logs

---

## 📊 Environment Variables Summary

### Backend (Vercel)

```
GEMINI_API_KEY=your-actual-gemini-api-key
FLASK_ENV=production
```

### Frontend (Vercel)

```
REACT_APP_API_URL=https://your-backend.vercel.app
```

---

## 🚀 Production Considerations

1. **Database:**

   - Current: SQLite (works for Vercel but data is ephemeral)
   - Recommended: Use Vercel Postgres or external database for persistence

2. **API Keys:**

   - Never commit API keys to git
   - Always use environment variables
   - Rotate keys periodically

3. **Rate Limiting:**

   - Consider adding rate limiting to API
   - Protect against abuse

4. **Monitoring:**

   - Use Vercel Analytics
   - Monitor API usage
   - Set up error tracking (Sentry)

5. **Custom Domain:**
   - Add custom domain in Vercel dashboard
   - Update CORS settings with new domain

---

## 📝 Next Steps After Deployment

1. **Test thoroughly:**

   - All FAQ categories
   - Different question types
   - Edge cases

2. **Monitor usage:**

   - Check Vercel Analytics
   - Monitor API response times
   - Track Gemini API usage

3. **Optimize:**

   - Enable caching where appropriate
   - Optimize bundle size
   - Add loading states

4. **Share:**
   - Share your live URL
   - Add to portfolio
   - Update GitHub README with live demo link

---

## 🔗 Useful Links

- Vercel Dashboard: https://vercel.com/dashboard
- Vercel Docs: https://vercel.com/docs
- Vercel Python Runtime: https://vercel.com/docs/runtimes#official-runtimes/python
- Your GitHub Repo: https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot

---

## 💡 Pro Tips

1. **Preview Deployments:** Every push to GitHub creates a preview deployment
2. **Environment Variables:** Can be different for Production/Preview/Development
3. **Vercel CLI:** Install for easier deployments: `npm i -g vercel`
4. **Logs:** Access real-time logs in Vercel dashboard
5. **Rollback:** Easy to rollback to previous deployments

---

**Need Help?**

- Vercel Support: https://vercel.com/support
- Vercel Community: https://github.com/vercel/vercel/discussions

---

**Good luck with your deployment! 🚀**
