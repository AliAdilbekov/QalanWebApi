import random

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
