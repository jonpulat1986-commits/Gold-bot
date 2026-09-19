from flask import Flask, request
import requests
import os
app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=data)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    final_msg = f"GOLD SIGNAL\n\n{data}"
    send_to_telegram(final_msg)
    return "ok", 200
@app.route('/')
def home():
    return "Bot ishlayapti"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
