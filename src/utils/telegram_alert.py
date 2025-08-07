import requests
from config import CERT_PATH, USE_CUSTOM_CERT

BOT_TOKEN = "7855951281:AAG5WG2QpNlapd0mmrob7F8ZOJxi5l51Mxc"
CHAT_ID = "-1002372063611"

def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    verify = CERT_PATH if USE_CUSTOM_CERT else False
    response = requests.post(url, json=payload, verify=verify)
    if response.status_code != 200:
        print(f"[ERROR] Telegram response: {response.text}")
    return response
