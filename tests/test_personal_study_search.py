import pytest
import allure
from utils.get_token import get_mentor_token
from api_clients.personal_study_client import PersonalStudyClient

phone = "77083544313"
expected_fullname = "Forautotest FORAUTOTEST"
expected_user_id = 1001
expected_subscription = "math_course"


@allure.title("Поиск ученика в Персональном обучении 2 (ПО2) по номеру телефона")
def test_search_pupil_in_po2():
    token = get_mentor_token()
    client = PersonalStudyClient()

    with allure.step(f"Отправляем запрос на /filteredBySearchText с номером {phone}"):
        response = client.search_by_phone(token, phone)
        assert response.status_code == 200, f"❌ Ошибка: {response.status_code} - {response.text}"
        data = response.json()
        assert isinstance(data, list) and data, "❌ Ученик не найден в ответе"

    with allure.step("Ищем ученика по номеру телефона"):
        pupil = next((item for item in data if item.get("phoneNumber") == phone), None)
        assert pupil, f"❌ Ученик с номером {phone} не найден в списке"

    with allure.step("Проверяем корректность данных ученика"):
        assert pupil["fullname"] == expected_fullname, "❌ Неверное имя"
        assert pupil["phoneNumber"] == phone, "❌ Неверный номер"
        assert pupil["userId"] == expected_user_id, "❌ Неверный userId"
        assert expected_subscription in pupil.get("allSubscriptionTypes", []), \
            f"❌ Подписка {expected_subscription} не найдена"

    with allure.step("✅ Ученик успешно найден в ПО2 и данные совпадают"):
        msg = f"[OK] Найден ученик: {pupil['fullname']} в ПО2 с подпиской {expected_subscription}"
        print(msg)
        allure.attach(msg, name="Результат поиска ПО2", attachment_type=allure.attachment_type.TEXT)


@allure.title("Поиск ученика в Персональном обучении 3 (ПО3) по номеру телефона")
def test_search_pupil_in_po3():
    token = get_mentor_token()
    client = PersonalStudyClient()

    with allure.step("Отправляем запрос на /mentorSessions"):
        response = client.get_mentor_sessions(token)
        assert response.status_code == 200, f"❌ Ошибка: {response.status_code} - {response.text}"
        data = response.json()
        assert isinstance(data, list) and data, "❌ Ответ не является валидным списком"

    with allure.step("Ищем ученика по номеру телефона"):
        pupil = next((item for item in data if item.get("phoneNumber") == phone), None)
        assert pupil, f"❌ Ученик с номером {phone} не найден в ПО3"

    with allure.step("Проверяем корректность данных ученика"):
        assert pupil["fullname"] == expected_fullname, "❌ Неверное имя"
        assert pupil["phoneNumber"] == phone, "❌ Неверный номер"
        assert pupil["userId"] == expected_user_id, "❌ Неверный userId"
        assert expected_subscription in pupil.get("allSubscriptionTypes", []), \
            f"❌ Подписка {expected_subscription} не найдена"

    with allure.step("✅ Ученик успешно найден в ПО3 и данные совпадают"):
        msg = f"[OK] Найден ученик: {pupil['fullname']} в ПО3 с подпиской {expected_subscription}"
        print(msg)
        allure.attach(msg, name="Результат поиска ПО3", attachment_type=allure.attachment_type.TEXT)
