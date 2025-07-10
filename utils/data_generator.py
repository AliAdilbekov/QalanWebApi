import random
from datetime import datetime
import pytz

kazakh_firstnames = [
    "Аян", "Нурислам", "Арман", "Айдос", "Ерасыл", "Даулет",
    "Алишер", "Санжар", "Ислам", "Нурсултан"
]

kazakh_surnames = [
    "Тлеубергенов", "Нурмаганбетов", "Есенгельдин", "Айтбаев",
    "Жаксылыков", "Калиев", "Оразалиев", "Кенжебаев", "Абишев", "Жумабаев"
]

def generate_phone_number():
    return "7708" + "".join(str(random.randint(0, 9)) for _ in range(7))

def generate_firstname():
    return random.choice(kazakh_firstnames)

def generate_surname():
    return random.choice(kazakh_surnames)


def generate_kaspi_check_link():
    # Алматыское время (GMT+6)
    almaty_tz = pytz.timezone("Asia/Almaty")

    # текущая дата-время в Алматы
    now_local = datetime.now(almaty_tz).replace(minute=0, second=0, microsecond=0)
    # Kaspi чек sale_date (локальное)
    sale_date = now_local.strftime("%Y-%m-%d+%H:%M:%S.32000")
    
    # paidAt (в UTC, ровно на 6 часов меньше)
    paid_at_utc = now_local.astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

    random_part = random.randint(1000000000, 9999999999)
    link = f"https://receipt.kaspi.kz/web?extTranId=QR{random_part}&sale_date={sale_date}"

    return {
        "kaspiCheckLink": link,
        "paidAt": paid_at_utc
    }

