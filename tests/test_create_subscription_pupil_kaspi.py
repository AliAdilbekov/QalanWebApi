import pytest
import allure
from src.utils.retry_utils import retry_on_failure
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.subscription_schemas import SubscriptionResponseSchema


@pytest.mark.parametrize("course_type, subscription_type, method_type, title", [
    ("math_course", "math_course", "kaspi_red", "Kaspi | kaspi_red"),
    ("math_course", "math_course", "kaspi_pay", "Kaspi | kaspi_pay (0.95%)"),
    ("math_course", "math_course", "kaspi_three_months", "Kaspi | kaspi_three_months"),
    ("math_course", "math_course", "kaspi_more_than_three_months", "Kaspi | kaspi_more_than_three_months"),
    ("math_course", "math_course", "kaspi_payments", "Kaspi | kaspi_payments (0.95%)"),
    ("math_course", "math_course", "kaspi_friday_24", "Kaspi | kaspi_friday_24"),
    ("unt_course", "math_course", "kaspi_red", "Kaspi | UNT курс"),
    ("english", "english", "kaspi_red", "Kaspi | English"),
])
@allure.title("Создание подписки через Kaspi: {title}")
def test_create_subscription_pupil_kaspi(
    admin_token,
    pupil_client,
    payment_client,
    pupil_payload,
    kaspi_subscription_payload,
    check_file_path,
    course_type,
    subscription_type,
    method_type,
    title
):
    with allure.step("Создаём ученика"):
        res = pupil_client.create_pupil(admin_token, pupil_payload["payload"])
        print(f"[DEBUG] Create Pupil Status: {res.status_code}")
        print(f"[DEBUG] Create Pupil Body: {res.text}")
        assert res.status_code == 200, f"{GlobalErrorMessages.CREATE_PUPIL_FAILED.value}: {res.text}"

        user_id = res.json().get("userId")
        assert user_id, GlobalErrorMessages.USER_ID_NOT_FOUND.value

    with allure.step("Формируем данные подписки через Kaspi"):
        form_data = kaspi_subscription_payload(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            course_type=course_type,
            subscription_type=subscription_type,
            method_type=method_type
        )
        print(f"[DEBUG] Subscription Form Data: {form_data}")
        print(f"[DEBUG] Check file path: {check_file_path}")

    @retry_on_failure(max_attempts=3, wait_seconds=2)
    def send_request_with_retry():
        res = payment_client.create_subscription(admin_token, form_data, check_file_path)
        print(f"[DEBUG] Subscription Status: {res.status_code}")
        print(f"[DEBUG] Subscription Body: {res.text}")
        assert res.status_code == 200, f"{GlobalErrorMessages.RETRY_FAIL.value}: {res.text}"
        return res

    res = send_request_with_retry()

    with allure.step("Валидируем ответ от /create-subscription"):
        data = SubscriptionResponseSchema.model_validate_json(res.text)
        assert data.is_success(), \
            f"{GlobalErrorMessages.SUBSCRIPTION_CREATION_FAILED.value}: ожидали 'ok', получили '{res.text}'"

    with allure.step("✅ Подписка через Kaspi успешно создана"):
        msg = f"[OK] Подписка «{title}» через Kaspi создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name=f"Kaspi Подписка {title}", attachment_type=allure.attachment_type.TEXT)
