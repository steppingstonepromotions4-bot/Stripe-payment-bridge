# Invoice Template - Access Guide

## ✅ Your Invoice is Now Integrated!

After deploying to Render, your invoice will be available at:

```
https://your-app-name.onrender.com/invoice
```

## 🎯 How It Works

1. **Invoice template automatically detects the domain** it's hosted on
2. **Payment button dynamically links** to the `/pay-invoice` endpoint on the same domain
3. **No manual URL updates needed** - it just works!

## 🔗 Access Points

After Render deployment, you'll have:

- **API Root:** `https://your-app.onrender.com/` 
  - Returns: "Invoice Bridge API OK"

- **Health Check:** `https://your-app.onrender.com/health`
  - Returns: `{"status":"ok","stripe_configured":true}`

- **Invoice Template:** `https://your-app.onrender.com/invoice`
  - Full interactive invoice form with payment button

- **Payment Endpoint:** `https://your-app.onrender.com/pay-invoice?amount=X&invoice_ref=Y`
  - Creates Stripe checkout session

## 📤 Sharing Invoices with Clients

### Option 1: Direct Link (Easiest)
Send clients the invoice URL:
```
https://your-app.onrender.com/invoice
```

They can:
- Fill in their details
- See the total
- Click "PAY IN FULL" to pay instantly

### Option 2: Prefilled Link
You can also create direct payment links:
```
https://your-app.onrender.com/pay-invoice?amount=5000&invoice_ref=INV-0123
```

This bypasses the invoice form and goes straight to Stripe checkout.

## 💾 Invoice Data Storage

The invoice template uses **browser localStorage**, so:
- ✅ Data persists when you reload the page
- ✅ Privacy-friendly (stored locally, not on server)
- ⚠️ Data is browser-specific (won't sync across devices)
- ⚠️ Clearing browser data will reset the form

## 🖨️ Generating PDFs

Clients can:
1. Fill out the invoice
2. Click "Print / Save as PDF"
3. Select "Save as PDF" in the print dialog
4. Get a professional PDF invoice

## 🔐 Security Notes

- The invoice template is **public** (anyone with the link can view it)
- Payment processing is **secure** (handled by Stripe)
- Stripe keys are **server-side only** (never exposed to client)
- Use Render environment variables for keys (never in code)

## 🎨 Customization

To customize the invoice template:
1. Edit `/Users/michaelnisanov/Desktop/invoice_bridge/templates/invoice.html`
2. Commit and push changes
3. Render auto-deploys the updates

Common customizations:
- Company name/logo
- Colors (CSS variables at top)
- Payment terms text
- Currency symbol

## ✨ Next Steps

1. **Deploy to Render** (if not done yet)
2. **Get your URL** (e.g., `https://invoice-bridge-abc123.onrender.com`)
3. **Visit** `https://your-url.onrender.com/invoice`
4. **Test** the payment flow
5. **Bookmark** or share with clients!

---

**Pro Tip:** You can create a custom domain (e.g., `invoice.yourbusiness.com`) in Render settings for a more professional look!
