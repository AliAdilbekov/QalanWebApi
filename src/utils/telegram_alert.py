import requests
import os

BOT_TOKEN = "7855951281:AAG5WG2QpNlapd0mmrob7F8ZOJxi5l51Mxc"
CHAT_ID = "-1002372063611"

def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}

    # Отключаем SSL в GitHub Actions
    verify = False if os.getenv("CI") == "true" else True

    try:
        response = requests.post(url, json=payload, verify=verify)
        if response.status_code != 200:
            print(f"[ERROR] Telegram response: {response.text}")
        return response
    except Exception as e:
        print(f"[WARNING] Telegram send failed: {e}")
