from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print("📩 Received Webhook")
    print(request.json)  # tampilkan data dari TradingView
    return "Webhook received", 200

@app.route("/")
def home():
    return "Hello Eggi Farhan!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
