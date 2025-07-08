import random
from faker import Faker

fake = Faker('ru_RU')  # Генератор русских имён

def generate_phone_number():
    return "7708" + "".join(str(random.randint(0, 9)) for _ in range(7))

def generate_firstname():
    return fake.first_name()

def generate_surname():
    return fake.last_name()
