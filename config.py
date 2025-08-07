import os

# если окружение не указывать, используется дефолт — preprod
ENV = os.getenv("ENV", "preprod")

BASE_URLS = {
    # "prod": "https://qalan.kz/api",
    "test": "https://test.qalan.kz/api",
    "preprod": "https://preprod.qalan.kz/api",
}

CERTS = {
    # "prod": "certs/qalan_prod.crt",
    "test": "certs/qalan_test.crt",
    "preprod": "certs/qalan_preprod.crt",
}

BASE_URL = BASE_URLS[ENV]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERT_PATH = os.path.join(BASE_DIR, CERTS[ENV])

# Отключаем кастомные сертификаты (временно)
USE_CUSTOM_CERT = False
