import pytest
import allure


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
        response = pupil_client.create_pupil(admin_token, pupil_payload["payload"])
        assert response.status_code == 200, f"❌ Ошибка создания ученика: {response.text}"
        user_id = response.json()["userId"]
        assert user_id, "❌ userId не найден"

    with allure.step("Формируем данные подписки через Kaspi"):
        form_data = kaspi_subscription_payload(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            course_type=course_type,
            subscription_type=subscription_type,
            method_type=method_type
        )

    with allure.step("Отправляем запрос"):
        response = payment_client.create_subscription(admin_token, form_data, check_file_path)
        assert response.status_code == 200, f"❌ Ошибка подписки: {response.text}"

    with allure.step("Готово"):
        msg = f"[OK] Подписка «{title}» через Kaspi создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name=f"Kaspi Подписка {title}", attachment_type=allure.attachment_type.TEXT)
