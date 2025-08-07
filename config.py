import os


BASE_URL = "https://preprod.qalan.kz/api"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERT_PATH = os.path.join(BASE_DIR, "certs", "qalan_preprod.crt")

# Использовать SSL-проверку или нет
USE_CUSTOM_CERT = False