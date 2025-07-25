import pytest
import allure
from src.enums.global_enums import GlobalErrorMessages

@allure.title("Создание сотрудника с ролью: sbb_employee")
def test_create_sbb_employee(admin_token, employee_client, employee_payload_template):
    with allure.step("Генерируем payload для обычного сотрудника"):
        payload = employee_payload_template(role="sbb_employee")
        expected_fields = {
            "firstname": payload["firstname"],
            "surname": payload["surname"],
            "phoneNumber": payload["phoneNumber"],
            "role": "sbb_employee",
            "department": payload["department"],
        }

    with allure.step("Создаём сотрудника через /employees"):
        response = employee_client.create_employee(admin_token, payload)
        assert response.status_code == 200, \
            f"{GlobalErrorMessages.EMPLOYEE_CREATION_FAILED.value} {response.text}"
        data = response.json()

    with allure.step("Проверяем, что данные совпадают"):
        for key, val in expected_fields.items():
            assert data[key] == val, \
                f"{GlobalErrorMessages.FIELD_MISMATCH.value}: '{key}' – ожидалось '{val}', получили '{data.get(key)}'"

    with allure.step("✅ Сотрудник успешно создан"):
        msg = f"[OK] Sbb Employee создан: {expected_fields['firstname']} {expected_fields['surname']}"
        print(msg)
        allure.attach(msg, name="Sbb Employee создан", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание ментора")
def test_create_mentor(admin_token, employee_client, mentor_payload_template):
    with allure.step("Генерируем payload для ментора"):
        payload = mentor_payload_template()
        expected_fields = {
            "firstname": payload["firstname"],
            "surname": payload["surname"],
            "phoneNumber": payload["phoneNumber"],
            "qualification": payload["qualification"],
            "department": payload["department"],
        }

    with allure.step("Создаём ментора через /mentors"):
        response = employee_client.create_mentor(admin_token, payload)
        assert response.status_code == 200, \
            f"{GlobalErrorMessages.MENTOR_CREATION_FAILED.value} {response.text}"
        data = response.json()

    with allure.step("Проверяем, что данные совпадают"):
        for key, val in expected_fields.items():
            assert data[key] == val, \
                f"{GlobalErrorMessages.FIELD_MISMATCH.value}: '{key}' – ожидалось '{val}', получили '{data.get(key)}'"

    with allure.step("✅ Ментор успешно создан"):
        msg = f"[OK] Mentor создан: {expected_fields['firstname']} {expected_fields['surname']}"
        print(msg)
        allure.attach(msg, name="Mentor создан", attachment_type=allure.attachment_type.TEXT)
