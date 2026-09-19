from flask import Flask, request
import requests
app = Flask(__name__)
8762867941:AAHE8WQWiSL4MG4C2nMO-k4KLj_UJmuVOF0
8182600595
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=data)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    final_msg = f"🔔 GOLD SIGNAL\n\n{data}\n\nTF: 15m | 1h trend"
    send_to_telegram(final_msg)
    return "ok", 200
@app.route('/')
def home():
    return "Bot ishlayapti"
