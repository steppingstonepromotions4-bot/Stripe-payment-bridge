from flask import Flask, redirect, request, url_for
import stripe
import os

app = Flask(__name__)

# --- 1. CONFIGURE YOUR STRIPE API KEY ---

# METHOD A: SECURE (RECOMMENDED) - The script reads the key from the Terminal.
# Make sure you ran 'export STRIPE_SECRET_KEY=...' in your Terminal.
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# METHOD B: DIRECT (FOR TESTING ONLY) - If Method A fails, use this instead.
# UNCOMMENT the line below and REPLACE the placeholder with your actual sk_live_... key.
# stripe.api_key = "sk_live_YOUR_ACTUAL_SECRET_KEY_HERE"


@app.route('/pay-invoice', methods=['GET'])
def create_stripe_session():
    # --- 2. READ DATA FROM YOUR HTML LINK (URL) ---
    # The 'amount' and 'invoice_ref' are the parameters sent by your HTML JavaScript
    
    # Reads the amount (in cents) and converts it to an integer
    amount_in_cents = request.args.get('amount', type=int) 
    
    # Reads the invoice reference number (e.g., '0005')
    invoice_ref = request.args.get('invoice_ref', default='INV-0000')

    # Basic check to ensure the amount is valid
    if not stripe.api_key:
        return "Error: Stripe API Key is not configured in the environment.", 500
    if amount_in_cents is None or amount_in_cents <= 0:
        return "Error 400: Payment amount missing or invalid in URL.", 400

    try:
        # --- 3. CREATE SECURE STRIPE CHECKOUT SESSION ---
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': amount_in_cents, # This is the dynamic amount from the HTML
                    'product_data': {
                        'name': f"Vortez Media Invoice Payment #{invoice_ref}",
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            # URLs to send the client to after successful or failed payment attempts
            success_url=request.url_root + 'success',
            cancel_url=request.url_root + 'cancel',
            client_reference_id=invoice_ref, # Links the payment back to your invoice number
        )
        
        # --- 4. REDIRECT THE CLIENT BROWSER TO STRIPE ---
        # This sends the client to the unique, secure Stripe URL
        return redirect(session.url, code=303)

    except Exception as e:
        # If Stripe returns an error (e.g., bad API key, wrong format)
        return f"An error occurred while communicating with Stripe: {str(e)}", 500

# Placeholder page for successful payment
@app.route('/success')
def payment_success():
    return "✅ Success! Your payment has been processed. Thank you for your business."

# Placeholder page for cancelled payment
@app.route('/cancel')
def payment_cancel():
    return "❌ Payment cancelled. Please return to the invoice and try again."

# This runs the server when you execute 'python app.py'
if __name__ == '__main__':
    print("Starting Flask app on http://127.0.0.1:5000/")
    app.run(debug=True, host='127.0.0.1', port=5000)