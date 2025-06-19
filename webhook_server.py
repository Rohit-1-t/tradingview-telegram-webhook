from flask import Flask, request
import requests

app = Flask(__name__)

bot_token = '8090668207:AAHBD-OM2W5ve22cchUvqFv6Eer_4aAkHwA'
chat_id = '1329952980'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '⚠️ No message!')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data={'chat_id': chat_id, 'text': message})
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(__import__('os').environ.get('PORT', 5000)))
