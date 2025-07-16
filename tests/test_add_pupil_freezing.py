import pytest
import allure
from utils.get_token import get_freezing_pupil_token
from api_clients.pupil_client import PupilClient
from utils.data_generator import generate_freezing_date

@allure.title("Добавление заморозки ученику")
def test_add_freezing_to_pupil():
    token = get_freezing_pupil_token()  # ← используем именно этот токен
    client = PupilClient()
    freeze_date = generate_freezing_date()

    with allure.step(f"Пробуем заморозить ученика на дату: {freeze_date}"):
        response = client.add_freezing(token, freeze_date)

        print(f"[DEBUG] STATUS: {response.status_code}")
        print(f"[DEBUG] BODY: {response.text}")

        if response.status_code == 406:
            error = response.json().get("error", {}).get("rus", "")
            assert "заморозка" in error, f"❌ Неожиданная ошибка: {error}"
            allure.attach(f"⚠️ Заморозка уже есть на дату {freeze_date}", "Инфо", allure.attachment_type.TEXT)
            pytest.skip(f"⚠️ Заморозка уже существует на {freeze_date}")

        assert response.status_code == 200, f"❌ Ошибка при заморозке: {response.status_code} - {response.text}"

        result = response.json()
        assert result.get("date") == freeze_date, \
            f"❌ Дата заморозки не совпадает: ожидалось {freeze_date}, получили {result.get('date')}"

    with allure.step("✅ Заморозка успешно добавлена"):
        msg = f"[OK] Заморозка установлена на {freeze_date}"
        print(msg)
        allure.attach(msg, name="Заморозка", attachment_type=allure.attachment_type.TEXT)
