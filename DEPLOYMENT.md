# Stripe Payment Bridge - Render Deployment Guide

## ✅ Pre-Deployment Checklist

Your repository is ready to deploy with:
- ✅ `app.py` - Flask application with health routes & logging
- ✅ `wsgi.py` - Gunicorn WSGI entry point
- ✅ `requirements.txt` - All dependencies (Flask, Stripe, Gunicorn)
- ✅ `.gitignore` - Excludes venv and system files

## 🚀 Step-by-Step Render Deployment

### 1. Sign Up / Log In to Render
- Go to: https://dashboard.render.com
- Sign up with GitHub (recommended for easier repo connection)

### 2. Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Select **"Connect a repository"** → Choose GitHub
3. Find and select: `steppingstonepromotions4-bot/Stripe-payment-bridge`
4. Click **"Connect"**

### 3. Configure Web Service

Fill in these settings:

**Basic Settings:**
```
Name: invoice-bridge
Region: US East (Ohio)  [or closest to your users]
Branch: main
Root Directory: [leave blank]
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn wsgi:application
```

**Instance Type:**
```
Free (for testing)
OR
Starter - $7/month (for production - no sleep, better performance)
```

### 4. Environment Variables (CRITICAL!)

Click **"Advanced"** → **"Add Environment Variable"**

Add this variable:

| Key | Value |
|-----|-------|
| `STRIPE_SECRET_KEY` | `sk_live_YOUR_ACTUAL_STRIPE_KEY_HERE` |

⚠️ **Security Note:** Use your actual Stripe live key here (starts with `sk_live_...`). Never commit this key to Git. Only add it in Render's dashboard.

### 5. Optional: Configure Health Check

Under **"Advanced"** → **"Health Check Path"**:
```
/health
```

This helps Render monitor your app and restart if needed.

### 6. Deploy!

Click **"Create Web Service"**

Render will:
1. Clone your repository
2. Install dependencies
3. Start gunicorn
4. Assign you a URL like: `https://invoice-bridge-abc123.onrender.com`

**Expected deploy time:** 2-3 minutes

### 7. Verify Deployment

Once you see **"Your service is live 🎉"**, test these endpoints:

```bash
# Health check (should return JSON with status)
curl https://your-app-name.onrender.com/health

# Root endpoint (should return "Invoice Bridge API OK")
curl https://your-app-name.onrender.com/

# Payment test (should redirect to Stripe - returns 303)
curl -L "https://your-app-name.onrender.com/pay-invoice?amount=100&invoice_ref=TEST-001"
```

## 🔗 Update Your Invoice HTML

After deployment, you'll receive a URL like:
```
https://invoice-bridge-abc123.onrender.com
```

**Update your HTML invoice template:**

Open `/Users/michaelnisanov/Desktop/invoice-template-2.html` and change:

```javascript
const BASE_STRIPE_URL = "https://your-app-name.onrender.com/pay-invoice";
```

To your actual Render URL:

```javascript
const BASE_STRIPE_URL = "https://invoice-bridge-abc123.onrender.com/pay-invoice";
```

Save and refresh your invoice page. The "PAY IN FULL" button will now work!

## 📊 Monitor Your App

**View Logs:**
- Render Dashboard → Your Service → "Logs" tab
- Shows startup logs, request logs, and any errors

**View Metrics:**
- "Metrics" tab shows CPU, memory, and request stats

**Manual Redeploy:**
- "Manual Deploy" → "Deploy latest commit"

## 🐛 Troubleshooting

### Issue: "Application failed to respond"
**Check:**
- Logs for Python import errors
- Environment variable `STRIPE_SECRET_KEY` is set correctly
- Start command is exactly: `gunicorn wsgi:application`

### Issue: "Module not found: stripe" or "Module not found: flask"
**Fix:**
- Verify Build Command: `pip install -r requirements.txt`
- Check `requirements.txt` is at repo root (not in venv/)
- Trigger manual redeploy

### Issue: Payment button doesn't work
**Check:**
1. HTML has correct Render URL (not localhost)
2. Parameter name is `invoice_ref` not `client_ref`
3. Amount is in cents (e.g., 100 for $1.00)
4. Stripe account is activated for live payments

### Issue: Free tier sleeps
**Behavior:**
- Free tier apps sleep after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake
- **Solution:** Upgrade to Starter ($7/mo) for always-on

## 🎯 Testing Payment Flow

1. Open your invoice HTML in browser
2. Fill in invoice details
3. Click "PAY IN FULL (CARD / BANK)"
4. Should redirect to: `https://your-app.onrender.com/pay-invoice?amount=...`
5. App logs the request (check Render logs)
6. Redirects to Stripe Checkout page
7. Complete test payment with Stripe test card: `4242 4242 4242 4242`
8. Redirects back to success/cancel page

## 📝 Next Steps

- [ ] Deploy to Render
- [ ] Test health endpoint
- [ ] Update HTML with Render URL
- [ ] Test end-to-end payment flow
- [ ] Monitor logs for first few transactions
- [ ] Consider upgrading to Starter tier for production

## 🔒 Security Best Practices

1. Never commit Stripe keys to Git
2. Use Stripe test keys (`sk_test_...`) during development
3. Only use live keys (`sk_live_...`) in Render environment variables
4. Enable Stripe webhook signing for production
5. Review Stripe dashboard regularly for suspicious activity

---

**Support:** If you encounter issues, check Render logs first. The app includes detailed logging for debugging.

**Repository:** https://github.com/steppingstonepromotions4-bot/Stripe-payment-bridge
