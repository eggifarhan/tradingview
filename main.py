from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Eggi Farhan!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Received Webhook:", data)
    return "Webhook received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
