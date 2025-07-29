import pytest
import allure
from src.utils.get_token import get_mentor_token
from src.api_clients.personal_study_client import PersonalStudyClient
from src.data.test_data.pupils import po_test_pupil
from src.schemas.personal_study_schemas import PersonalStudyPupilSchema
from src.enums.global_enums import GlobalErrorMessages
from src.utils.helpers import validate_personal_study_pupil


@allure.title("Поиск ученика в Персональном обучении 2 (ПО2) по номеру телефона")
def test_search_pupil_in_po2():
    token = get_mentor_token()
    client = PersonalStudyClient()
    expected = po_test_pupil

    with allure.step(f"Запрос на /filteredBySearchText с номером {expected['phone']}"):
        res = client.search_by_phone(token, expected["phone"])
        print(f"[DEBUG] Status: {res.status_code}")
        print(f"[DEBUG] Body: {res.text}")

        assert res.status_code == 200, GlobalErrorMessages.RESPONSE_STATUS_ERROR.value.format(
            status=res.status_code, body=res.text)

        pupils = res.json()
        assert isinstance(pupils, list) and pupils, GlobalErrorMessages.USER_NOT_FOUND_IN_RESPONSE.value

    with allure.step("Находим нужного ученика по номеру"):
        matched = next((p for p in pupils if p.get("phoneNumber") == expected["phone"]), None)
        print(f"[DEBUG] Найденный ученик: {matched}")
        assert matched, GlobalErrorMessages.USER_NOT_FOUND_IN_LIST.value.format(phone=expected["phone"])

        pupil = PersonalStudyPupilSchema.model_validate(matched)

    with allure.step("Валидируем данные ученика"):
        validate_personal_study_pupil(pupil, expected)

    with allure.step("✅ Ученик в ПО2 успешно найден и проверен"):
        msg = f"[OK] Найден ученик: {pupil.fullname} в ПО2 с подпиской {expected['subscription']}"
        print(msg)
        allure.attach(msg, name="Результат поиска ПО2", attachment_type=allure.attachment_type.TEXT)


@allure.title("Поиск ученика в Персональном обучении 3 (ПО3) по номеру телефона")
def test_search_pupil_in_po3():
    token = get_mentor_token()
    client = PersonalStudyClient()
    expected = po_test_pupil

    with allure.step("Запрос на /mentorSessions"):
        res = client.get_mentor_sessions(token)
        print(f"[DEBUG] Status: {res.status_code}")
        print(f"[DEBUG] Body: {res.text}")

        assert res.status_code == 200, GlobalErrorMessages.RESPONSE_STATUS_ERROR.value.format(
            status=res.status_code, body=res.text)

        pupils = res.json()
        assert isinstance(pupils, list) and pupils, GlobalErrorMessages.RESPONSE_NOT_LIST.value

    with allure.step("Находим нужного ученика по номеру"):
        matched = next((p for p in pupils if p.get("phoneNumber") == expected["phone"]), None)
        print(f"[DEBUG] Найденный ученик: {matched}")
        assert matched, GlobalErrorMessages.USER_NOT_FOUND_IN_LIST.value.format(phone=expected["phone"])

        pupil = PersonalStudyPupilSchema.model_validate(matched)

    with allure.step("Валидируем данные ученика"):
        validate_personal_study_pupil(pupil, expected)

    with allure.step("✅ Ученик в ПО3 успешно найден и проверен"):
        msg = f"[OK] Найден ученик: {pupil.fullname} в ПО3 с подпиской {expected['subscription']}"
        print(msg)
        allure.attach(msg, name="Результат поиска ПО3", attachment_type=allure.attachment_type.TEXT)
