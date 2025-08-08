# Qalan API Tests

Репозиторий автотестов для API-платформы [qalan.kz](https://preprod.qalan.kz)

---

## 📂 Структура проекта

```
qalan_api_tests/
│
├── allure-report/         # Сгенерированные отчёты Allure (не редактировать вручную)
│   └── ...                # Вспомогательные файлы, html-отчёты, вложения и т.д.
│
├── allure-results/        # Сырые результаты тестов для Allure (генерируются автоматически)
│   └── ...                # JSON и TXT файлы с результатами и логами тестов
│
├── certs/                 # Сертификаты для тестирования (если требуется) - сейчас требуется у windows есть проблема с этим 
│
├── src/                   # Исходный код вспомогательных модулей для тестов
│   ├── api_clients/       # Реализации клиентов для различных API
│   │   ├── __init__.py
│   │   ├── auth_client.py         # Клиент для аутентификации
│   │   ├── base_api_client.py     # Базовый класс для всех API-клиентов
│   │   └── ...                    # Другие клиенты для разных сервисов
│   │
│   ├── data/
│   │   └── test_data/
│   │       └── pupils.py          # Тестовые данные для учеников
│   │
│   ├── enums/
│   │   └── global_enums.py        # Глобальные перечисления для тестов и клиентов
│   │
│   ├── schemas/                   # Pydantic-схемы для валидации и сериализации данных
│   │   ├── chat_schemas.py
│   │   ├── employee_schemas.py
│   │   ├── freezing_schemas.py
│   │   └── ...                    # Схемы для других сущностей
│   │
│   └── utils/                     # Вспомогательные утилиты и генераторы
│       ├── check_for_payments/
│       │   └── check.png          # Пример вложенного ресурса
│       ├── data_generator.py      # Генератор тестовых данных
│       ├── get_token.py           # Получение токенов для тестов
│       ├── helpers.py             # Общие вспомогательные функции
│       └── ...                    # Прочие утилиты
│
├── tests/                  # Основные тестовые сценарии и фикстуры
│   ├── fixtures/           # Фикстуры для тестов (авторизация, подготовка данных и т.д.)
│   │   ├── auth_login_fixtures.py
│   │   ├── auth_register_fixtures.py
│   │   ├── chat_fixtures.py
│   │   └── ...             # Прочие фикстуры
│   │
│   ├── test_add_pupil_freezing.py     # Тесты по заморозке учеников
│   ├── test_chat_mentor_pupil.py      # Тесты чата между ментором и учеником
│   ├── test_create_employee.py        # Тесты создания сотрудников
│   └── ...                            # Прочие тестовые сценарии
│
├── config.py               # Конфигурация проекта (пути, параметры, переменные окружения)
├── conftest.py             # Глобальные фикстуры и хуки для pytest
├── requirements.txt        # Зависимости проекта (Python-библиотеки)
├── README.md               # Описание проекта (этот файл)
└── venv/                   # Виртуальное окружение Python (не включать в git)
```

---

## Описание ключевых папок и файлов

### allure-report/ и allure-results/
- Используются для хранения отчётов и результатов тестов Allure.
- Не изменяются вручную, могут быть добавлены в .gitignore.

### certs/
- Сертификаты для тестирования защищённых соединений (если используются).

### src/
- **api_clients/** — клиенты для различных API, каждый реализует методы для работы с определённым сервисом.
- **data/test_data/** — статические или сгенерированные тестовые данные.
- **enums/** — перечисления, используемые в тестах и клиентах (например, статусы, типы ролей).
- **schemas/** — Pydantic-схемы для валидации входных/выходных данных API.
- **utils/** — вспомогательные скрипты, генераторы данных, функции для получения токенов, общие хелперы.

### tests/
- **fixtures/** — фикстуры для подготовки тестовых данных, авторизации, мокирования и т.д.
- **test_*.py** — файлы с тестовыми сценариями, сгруппированные по функционалу.

### Корневые файлы
- **config.py** — глобальная конфигурация (пути, параметры, переменные окружения).
- **conftest.py** — глобальные фикстуры и хуки для pytest.
- **requirements.txt** — список зависимостей Python.
- **README.md** — описание проекта (вы читаете этот файл).
- **venv/** — виртуальное окружение Python (не включать в git).

---

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd qalan_api_tests
```

---

### 2. Создание и активация виртуального окружения

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

---

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

### 4. Запуск всех тестов

```bash
pytest -s -v tests/
```

---

### 5. Запуск отдельного теста

```bash
pytest -s -v tests/test_login.py
```

---

### 6. Запуск одного теста по имени функции

```bash
pytest -s -v tests/test_login.py::test_login_success
```

---

### 7. Генерация Allure-отчёта

#### 7.1. Запуск тестов с сохранением результатов для Allure

```bash
pytest --alluredir=allure-results -s -v tests/
```

#### 7.2. Генерация и просмотр отчёта Allure

```bash
allure serve allure-results
```
или
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

> **Примечание:** Для работы с Allure необходима установленная утилита Allure Commandline.
> Установить её можно, например, через Homebrew (macOS) или Chocolatey (Windows):

#### macOS (через Homebrew):

```bash
brew install allure
```

#### Windows (через Chocolatey):

```cmd
choco install allurecommandline
```

---

## Полезные команды

| Операция                        | Команда (macOS/Linux)                        | Команда (Windows)                        |
|----------------------------------|----------------------------------------------|------------------------------------------|
| Активация виртуального окружения | `source venv/bin/activate`                   | `venv\Scripts\activate`                  |
| Установка зависимостей           | `pip install -r requirements.txt`            | `pip install -r requirements.txt`        |
| Запуск всех тестов               | `pytest -s -v tests/`                        | `pytest -s -v tests/`                    |
| Запуск одного теста              | `pytest -s -v tests/test_login.py`           | `pytest -s -v tests/test_login.py`       |
| Запуск теста по функции          | `pytest -s -v tests/test_login.py::test_fn`  | `pytest -s -v tests/test_login.py::test_fn` |
| Запуск с Allure                  | `pytest --alluredir=allure-results ...`      | `pytest --alluredir=allure-results ...`  |
| Генерация и просмотр отчёта      | `allure serve allure-results`                | `allure serve allure-results`            |

---

## Примечания

- Все тесты написаны с использованием `pytest`.
- Для генерации отчётов используется Allure.
- Архитектура позволяет легко добавлять новые API-клиенты, схемы и тестовые сценарии.
- Для расширения тестов рекомендуется придерживаться текущей структуры: выносить логику работы с API в отдельные клиенты, использовать схемы для валидации, хранить тестовые данные отдельно.

---

## Требования

- **Python** 3.8 или выше  
- **pip** (обычно входит в стандартную поставку Python)
- **Allure Commandline** для генерации отчётов ([инструкция по установке](https://docs.qameta.io/allure/#_installing_a_commandline))

---

## Конфигурация

Перед запуском тестов убедитесь, что все необходимые параметры указаны в файле `config.py`.  
Если проект использует переменные окружения (например, для токенов, URL, путей к сертификатам), создайте файл `.env` в корне проекта по примеру:

```
BASE_URL=https://preprod.qalan.kz
API_TOKEN=your_token_here
CERT_PATH=certs/your_cert.pem
```

---

## Известные проблемы

- **Windows:**  
  Возможны ошибки, связанные с сертификатами (папка `certs/`). Проверьте, что путь к сертификатам корректно указан в `config.py` или переменных окружения. Иногда помогает запуск от имени администратора.
- **Allure не найден:**  
  Убедитесь, что allure установлен и добавлен в переменную PATH. Проверьте командой `allure --version`.

---

## Как добавить новый тест

1. Создайте новый файл в папке `tests/` с именем по шаблону `test_<feature>.py`.
2. Используйте существующие фикстуры из `tests/fixtures/` или добавьте свои.
3. Для работы с API используйте соответствующий клиент из `src/api_clients/`.
4. Для валидации данных используйте схемы из `src/schemas/`.
5. Пример теста:
    ```python
    def test_example(auth_client, valid_login_payload):
        response = auth_client.login(valid_login_payload)
        assert response.status_code == 200
    ```

---

## FAQ

**Q:** Как посмотреть Allure-отчёт, если не открывается в браузере?  
**A:** Проверьте, что порт 8080 свободен, или используйте команду `allure open allure-report` для открытия в браузере по умолчанию.

**Q:** Как запустить только один тест?  
**A:**  
```bash
pytest -s -v tests/test_login.py::test_login_success
```

---

запуск с разных env
ENV=test pytest -s -v tests/
ENV=preprod pytest -s -v tests/

