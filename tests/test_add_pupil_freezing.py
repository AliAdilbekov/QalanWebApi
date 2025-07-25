import pytest
import allure
from src.utils.get_token import get_freezing_pupil_token
from src.api_clients.pupil_client import PupilClient
from src.utils.data_generator import generate_freezing_date
from src.enums.global_enums import GlobalErrorMessages

@allure.title("Добавление заморозки ученику")
def test_add_freezing_to_pupil():
    token = get_freezing_pupil_token()
    client = PupilClient()
    freeze_date = generate_freezing_date()

    with allure.step(f"Пробуем заморозить ученика на дату: {freeze_date}"):
        response = client.add_freezing(token, freeze_date)

        print(f"[DEBUG] STATUS: {response.status_code}")
        print(f"[DEBUG] BODY: {response.text}")

        if response.status_code == 406:
            error = response.json().get("error", {}).get("rus", "")
            assert "заморозка" in error, f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value}: {error}"
            allure.attach(
                f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value} {freeze_date}",
                "Инфо",
                allure.attachment_type.TEXT
            )
            pytest.skip(f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value} {freeze_date}")

        assert response.status_code == 200, f"{GlobalErrorMessages.FREEZING_FAILED.value} {response.status_code} - {response.text}"

        result = response.json()
        assert result.get("date") == freeze_date, \
            f"{GlobalErrorMessages.FREEZING_DATE_MISMATCH.value} ожидалось {freeze_date}, получили {result.get('date')}"

    with allure.step("✅ Заморозка успешно добавлена"):
        msg = f"[OK] Заморозка установлена на {freeze_date}"
        print(msg)
        allure.attach(msg, name="Заморозка", attachment_type=allure.attachment_type.TEXT)
