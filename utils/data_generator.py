import random
from datetime import datetime
from datetime import datetime, timedelta
import pytz

kazakh_firstnames = [
    "Аян", "Нурислам", "Арман", "Айдос", "Ерасыл", "Даулет",
    "Алишер", "Санжар", "Ислам", "Нурсултан",
    "Ержан", "Темирлан", "Бекзат", "Жанболат", "Еркебулан",
    "Аскар", "Алмат", "Мирас", "Бауржан", "Жандос",
    "Мадияр", "Жасулан", "Айбек", "Рустам", "Ануар",
    "Ермек", "Елдос", "Ерасылхан", "Сырым", "Берик",
    "Куаныш", "Олжас", "Шерхан", "Талгат", "Жанибек"
]

kazakh_surnames = [
    "Тлеубергенов", "Нурмаганбетов", "Есенгельдин", "Айтбаев",
    "Жаксылыков", "Калиев", "Оразалиев", "Кенжебаев", "Абишев", "Жумабаев",
    "Сатыбалдиев", "Бекмуратов", "Есимов", "Сагындыков", "Кожахметов",
    "Турсынов", "Токтасынов", "Абдрахманов", "Мусин", "Тажибаев",
    "Аубакиров", "Амангельдиев", "Нуртазин", "Жумагулов", "Серикбаев",
    "Даулетбаев", "Ахметов", "Калмурзаев", "Бердигулов", "Баймуханов"
]


def generate_phone_number():
    prefix = random.choice(["7708", "7707", "7777", "7702", "7778"])
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(7))


def generate_firstname():
    return random.choice(kazakh_firstnames)

def generate_surname():
    return random.choice(kazakh_surnames)


def generate_kaspi_check_link():
    # Алматы время (GMT+6)
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


def generate_freezing_date():
    start = datetime(2025, 7, 16)
    end = datetime(2026, 4, 30)
    delta = end - start
    random_day = random.randint(0, delta.days)
    result_date = start + timedelta(days=random_day)
    return result_date.strftime("%Y-%m-%d")


def generate_unique_chat_message_pupil() -> str:
    return f"hello pupil {random.randint(1000, 9999)}"

def generate_unique_chat_message_mentor() -> str:
    return f"hello mentor {random.randint(1000, 9999)}"