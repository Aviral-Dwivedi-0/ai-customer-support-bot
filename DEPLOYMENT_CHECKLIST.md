# ✅ Vercel Deployment Checklist

Use this checklist to track your deployment progress:

## 📋 Pre-Deployment

- [ ] Code pushed to GitHub
- [ ] Have Gemini API key ready
- [ ] Vercel account created (sign up at vercel.com with GitHub)

## 🔧 Backend Deployment

- [ ] Go to vercel.com/new
- [ ] Import ai-customer-support-bot repository
- [ ] Set Root Directory to `backend`
- [ ] Set Framework to "Other"
- [ ] Add environment variable: `GEMINI_API_KEY`
- [ ] Add environment variable: `FLASK_ENV=production`
- [ ] Click Deploy
- [ ] Copy backend URL (e.g., https://ai-support-backend.vercel.app)
- [ ] Test backend: Visit backend URL in browser

## 🎨 Frontend Setup

- [ ] Update `frontend/src/App.js` with backend URL
- [ ] Change `API_URL` to use `process.env.REACT_APP_API_URL`
- [ ] Commit and push changes to GitHub

## 🚀 Frontend Deployment

- [ ] Go to vercel.com/new again
- [ ] Import ai-customer-support-bot repository (same repo, different project)
- [ ] Set Root Directory to `frontend`
- [ ] Set Framework to "Create React App"
- [ ] Add environment variable: `REACT_APP_API_URL` with backend URL
- [ ] Click Deploy
- [ ] Copy frontend URL (e.g., https://ai-support-frontend.vercel.app)

## 🔒 CORS Configuration

- [ ] Update `backend/app/main.py` CORS origins
- [ ] Add frontend Vercel URL to allowed origins
- [ ] Commit and push changes
- [ ] Wait for auto-redeploy

## ✅ Testing

- [ ] Open frontend URL in browser
- [ ] Test chat functionality
- [ ] Ask sample questions from FAQ
- [ ] Verify responses are accurate
- [ ] Check browser console for errors (F12)

## 🎯 Post-Deployment

- [ ] Monitor Vercel dashboard for errors
- [ ] Test from different devices
- [ ] Update README with live demo link
- [ ] Share your deployed chatbot!

---

## 📝 Important URLs to Save

**Backend URL:** ******************\_\_\_******************

**Frontend URL:** ******************\_\_\_******************

**GitHub Repo:** https://github.com/Aviral-Dwivedi-0/ai-customer-support-bot

**Vercel Dashboard:** https://vercel.com/dashboard

---

## 🆘 If Something Goes Wrong

**Backend not working?**

- Check Vercel logs: Dashboard → Backend Project → Functions
- Verify GEMINI_API_KEY is set
- Test with: `curl https://your-backend.vercel.app`

**Frontend can't connect to backend?**

- Check REACT_APP_API_URL is correct
- Verify CORS is configured
- Check browser console (F12) for errors

**Chat not responding?**

- Check both backend and frontend are deployed
- Verify API_URL in frontend matches backend URL
- Test backend API directly

---

**Need help?** Check VERCEL_DEPLOYMENT_GUIDE.md for detailed instructions!
