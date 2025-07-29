import pytest
import allure
from src.utils.get_token import get_freezing_pupil_token
from src.api_clients.pupil_client import PupilClient
from src.utils.data_generator import generate_freezing_date
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.freezing_schemas import AddFreezingResponse


@allure.title("Добавление заморозки ученику")
def test_add_freezing_to_pupil():
    token = get_freezing_pupil_token()
    client = PupilClient()
    freeze_date = generate_freezing_date()

    with allure.step(f"Пробуем заморозить ученика на дату: {freeze_date}"):
        res = client.add_freezing(token, freeze_date)

        if res.status_code == 406:
            error_msg = res.json().get("error", {}).get("rus", "")
            assert "заморозка" in error_msg, f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value}: {error_msg}"
            allure.attach(
                f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value} {freeze_date}",
                name="Заморозка уже существует",
                attachment_type=allure.attachment_type.TEXT
            )
            pytest.skip(f"{GlobalErrorMessages.FREEZING_ALREADY_EXISTS.value} {freeze_date}")

        assert res.status_code == 200, f"{GlobalErrorMessages.FREEZING_FAILED.value}: {res.status_code} - {res.text}"

        freezing = AddFreezingResponse.model_validate(res.json())
        assert freezing.date == freeze_date, \
            f"{GlobalErrorMessages.FREEZING_DATE_MISMATCH.value}: ожидалось {freeze_date}, получили {freezing.date}"

    with allure.step("✅ Заморозка успешно добавлена"):
        msg = f"[OK] Заморозка установлена на {freeze_date}"
        print(msg)
        allure.attach(msg, name="Заморозка", attachment_type=allure.attachment_type.TEXT)
