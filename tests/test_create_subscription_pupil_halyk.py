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

    with allure.step("Готовим данные для подписки через Halyk"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank" 
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка через Halyk создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка (Halyk)", attachment_type=allure.attachment_type.TEXT)



@allure.title("Создание подписки ученику через Halyk Bank (рассрочка на 3 месяца)")
def test_create_subscription_pupil_halyk_three_month(
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

    with allure.step("Готовим данные для подписки через Halyk (3 мес. рассрочка)"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank_three_month"
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка через Halyk (3 мес.) создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка Halyk (3 мес.)", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание подписки ученику через Halyk Bank (рассрочка на 6 месяцев)")
def test_create_subscription_pupil_halyk_six_month(
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

    with allure.step("Готовим данные для подписки через Halyk (6 мес. рассрочка)"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank_six_month"
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка через Halyk (6 мес.) создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка Halyk (6 мес.)", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание подписки ученику через Halyk Bank (рассрочка на 12 месяцев)")
def test_create_subscription_pupil_halyk_twelve_month(
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

    with allure.step("Готовим данные для подписки через Halyk (12 мес. рассрочка)"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank_twelve_month"
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка через Halyk (12 мес.) создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка Halyk (12 мес.)", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание подписки ученику через Halyk Bank (рассрочка на 24 месяца)")
def test_create_subscription_pupil_halyk_24_month(
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

    with allure.step("Готовим данные для подписки через Halyk (24 мес. рассрочка)"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank_24_month"
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка через Halyk (24 мес.) создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка Halyk (24 мес.)", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание подписки ученику на UNT курс через Halyk Bank")
def test_create_subscription_pupil_halyk_unt_course(
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

    with allure.step("Готовим данные для подписки на UNT курс"):
        form_data = subscription_payload_template(
            user_id=user_id,
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank",
            course_type="unt_course",
            subscription_type="math_course"
        )

        file_path = os.path.join(
            "utils",
            "check_for_payments",
            "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

    with allure.step("Отправляем запрос на создание подписки"):
        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Успешное завершение теста"):
        msg = f"[OK] Подписка (UNT курс) через Halyk создана для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка UNT (Halyk)", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание подписки ученику на курс English через Halyk Bank")
def test_create_subscription_pupil_english_halyk(
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
            pupil_phone=pupil_payload["expected"]["phone"],
            method_type="halyq_bank",
            course_type="english",
            subscription_type="english"
        )

        file_path = os.path.join(
            "utils", "check_for_payments", "Снимок экрана 2025-07-09 в 1.28.54 PM.png"
        )

        response = payment_client.create_subscription(admin_token, form_data, file_path)
        assert response.status_code == 200, f"❌ Ошибка при создании подписки: {response.text}"

    with allure.step("Подписка успешно оформлена"):
        msg = f"[OK] Подписка на английский оформлена для {pupil_payload['expected']['phone']}"
        print(msg)
        allure.attach(msg, name="Подписка (English)", attachment_type=allure.attachment_type.TEXT)
