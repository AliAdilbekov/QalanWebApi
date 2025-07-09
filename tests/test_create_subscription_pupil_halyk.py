import allure
import os

@allure.title("Создание подписки ученику через Halyk Bank")
def test_create_subscription_pupil_halyk(
    admin_token,
    pupil_client,
    payment_client,
    pupil_payload,
    subscription_payload_template
):
    with allure.step("Создаём ученика"):
        response = pupil_client.create_pupil(admin_token, pupil_payload["payload"])
        assert response.status_code == 200, f"❌ Ошибка создания ученика: {response.text}"
        user_id = response.json().get("userId")
        assert user_id, "❌ userId не найден в ответе"

    with allure.step("Создаём подписку"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"]
        )

        file_path = os.path.join(
            "utils", "check_for_payments", "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешно"):
        msg = f"[OK] Подписка через Halyk создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка (Halyk)", attachment_type=allure.attachment_type.TEXT)
