import os
import pytest
import allure
from src.utils.retry_utils import retry_on_failure
from src.enums.global_enums import GlobalErrorMessages


@pytest.mark.parametrize("method_type, course_type, subscription_type, title", [
    ("halyq_bank", "math_course", "math_course", "Halyk обычный"),
    ("halyq_bank_three_month", "math_course", "math_course", "Halyk 3 мес."),
    ("halyq_bank_six_month", "math_course", "math_course", "Halyk 6 мес."),
    ("halyq_bank_twelve_month", "math_course", "math_course", "Halyk 12 мес."),
    ("halyq_bank_24_month", "math_course", "math_course", "Halyk 24 мес."),
    ("halyq_bank", "unt_course", "math_course", "UNT курс"),
    ("halyq_bank", "english", "english", "English курс"),
])
@allure.title("Создание подписки ученику: {title}")
def test_create_subscription(
    admin_token,
    pupil_client,
    payment_client,
    pupil_payload,
    subscription_payload_template,
    check_file_path,
    method_type,
    course_type,
    subscription_type,
    title
):
    with allure.step("Создаём ученика"):
        response = pupil_client.create_pupil(admin_token, pupil_payload["payload"])
        assert response.status_code == 200, f"{GlobalErrorMessages.CREATE_PUPIL_FAILED.value}: {response.text}"
        user_id = response.json().get("userId")
        assert user_id, GlobalErrorMessages.USER_ID_NOT_FOUND.value

    with allure.step("Готовим данные подписки"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type=method_type,
            course_type=course_type,
            subscription_type=subscription_type
        )

    
    @retry_on_failure(max_attempts=3, wait_seconds=2)
    def send_request_with_retry():
        response = payment_client.create_subscription(admin_token, form_data, check_file_path)
        assert response.status_code == 200, f"{GlobalErrorMessages.RETRY_FAIL.value}: {response.text}"
        return response

    response = send_request_with_retry()

    with allure.step("Готово"):
        msg = f"[OK] Подписка «{title}» создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name=f"Подписка {title}", attachment_type=allure.attachment_type.TEXT)
