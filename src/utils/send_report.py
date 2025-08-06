import requests
import json
from config import CERT_PATH, USE_CUSTOM_CERT

BOT_TOKEN = "7855951281:AAG5WG2QpNlapd0mmrob7F8ZOJxi5l51Mxc"
CHAT_ID = "-1002372063611"
ALLURE_URL = "http://192.168.1.233:8888"

verify = CERT_PATH if USE_CUSTOM_CERT else False

def send_allure_summary():
    with open("allure-report/widgets/summary.json") as f:
        summary = json.load(f)

    total = summary["statistic"]["total"]
    passed = summary["statistic"]["passed"]
    failed = summary["statistic"]["failed"]
    skipped = summary["statistic"]["skipped"]
    time = summary["time"]["duration"] // 1000

    minutes = time // 60
    seconds = time % 60

    percent_passed = int((passed / total) * 100) if total else 0

    text = (
        "<b>🧪 Autotest Report API</b>\n\n"
        f"<b>🌐 Окружение:</b> <code>preprod</code>\n"
        f"<b>⏱ Продолжительность:</b> {minutes:02}:{seconds:02}\n"
        f"<b>📦 Тестов:</b> {total}\n"
        f"<b>✅ Успешных:</b> {passed} ({percent_passed}%)\n"
        f"<b>📄 Allure Report:</b> <a href='{ALLURE_URL}'>{ALLURE_URL}</a>\n"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    send_message_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(send_message_url, json=payload, verify=verify)
    print(f"[DEBUG] Telegram text status: {r.status_code}, {r.text}")

def send_allure_file():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    file_path = "allure-report/widgets/summary.json"

    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": CHAT_ID, "caption": "📎 summary.json"}
        r = requests.post(url, data=data, files=files, verify=verify)
        print(f"[DEBUG] Telegram file status: {r.status_code}, {r.text}")

if __name__ == "__main__":
    send_allure_summary()
    send_allure_file()
