# Qalan_API_Autotests
Репозиторий автотестов для API-платформы [qalan.kz](https://preprod.qalan.kz)

## 📂 Структура проекта

```

qalan\_api\_tests/
├── api\_clients/         # Обёртки для API-запросов (логин, регистрация и т.д.)
│   ├── base\_api\_client.py
│   └── auth\_client.py
│
├── tests/               # Сами автотесты
│   └── test\_register.py
│   └── test\_login.py
│
├── utils/               # Вспомогательные функции (генераторы, хелперы)
│   └── data\_generator.py
│
├── conftest.py          # Фикстуры pytest (данные и клиенты для тестов)
├── config.py            # Настройки, BASE\_URL и др.
└── requirements.txt     # Зависимости проекта

````

---

## ⚙️ Установка

```bash
git clone https://github.com/your-user/qalan_api_tests.git
cd qalan_api_tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## Запуск тестов

```bash
pytest -s tests/
```

С включённым Allure-репортом:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Компоненты

### `api_clients/`

Содержит API-клиенты. Каждый клиент — это обёртка для конкретной группы эндпоинтов.

Пример:

```python
class AuthClient(BaseAPIClient):
    def login(self, payload):
        return self.post("/users/login", json=payload)
```

---

### `conftest.py`

Содержит `pytest` фикстуры:

* `auth_client` — инициализация клиента
* `valid_login_payload` — валидные данные для логина
* `valid_register_payload` — данные для регистрации

---

### `tests/`

Содержит сами тесты

Каждый тест проверяет:

* статус ответа
* токен
* user-данные (имя, фамилия, номер и т.д.)

---

### `utils/`

Утилиты (генераторы случайных данных, вспомогательные функции)

```python
generate_phone_number()
generate_firstname()
generate_surname()
```

---

