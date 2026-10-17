from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Business information
BUSINESS_INFO = {
    "name": "Smart Store",
    "hours": "Monday to Saturday, 9 AM to 6 PM",
    "products": "Headphones, keyboards, and computer accessories",
    "headphones_price": "Rs. 999",
    "delivery": "Delivery is available within 3-5 business days",
    "order": "Please contact support with your order ID for order updates",
    "support": "Email us at support@smartstore.example"
}


def get_response(message):
    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to Smart Store. How can I help you?"

    elif "hour" in message or "time" in message or "open" in message:
        return f"Our working hours are {BUSINESS_INFO['hours']}."

    elif "product" in message or "sell" in message or "available" in message:
        return f"We offer {BUSINESS_INFO['products']}."

    elif "headphone" in message and ("price" in message or "cost" in message or "how much" in message):
        return f"Our headphones cost {BUSINESS_INFO['headphones_price']}."

    elif "deliver" in message or "shipping" in message:
        return BUSINESS_INFO["delivery"] + "."

    elif "order" in message or "track" in message:
        return BUSINESS_INFO["order"] + "."

    elif "contact" in message or "support" in message or "email" in message:
        return BUSINESS_INFO["support"] + "."

    elif "thank" in message:
        return "You're welcome! Is there anything else I can help you with?"

    else:
        return (
            "Sorry, I don't have that information right now. "
            "Please contact our customer support team for assistance."
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"reply": "Please enter a question."}), 400

    reply = get_response(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)