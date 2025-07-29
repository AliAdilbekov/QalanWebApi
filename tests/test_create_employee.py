import pytest
import allure
from pydantic import TypeAdapter

from src.enums.global_enums import GlobalErrorMessages
from src.schemas.employee_schemas import EmployeeCreateResponseSchema
from src.schemas.mentor_schemas import MentorCreateResponseSchema
from src.utils.helpers import (
    extract_expected_employee_fields,
    extract_expected_mentor_fields,
)


@allure.title("Создание сотрудника с ролью: sbb_employee")
def test_create_sbb_employee(admin_token, employee_client, employee_payload_template):
    payload = employee_payload_template(role="sbb_employee")
    expected = extract_expected_employee_fields(payload)
    adapter = TypeAdapter(EmployeeCreateResponseSchema)

    with allure.step("Создаём сотрудника через /employees"):
        res = employee_client.create_employee(admin_token, payload)
        assert res.status_code == 200, \
            f"{GlobalErrorMessages.EMPLOYEE_CREATION_FAILED.value}: {res.text}"
        employee = adapter.validate_python(res.json())

    with allure.step("Проверяем ключевые поля ответа"):
        for key, val in expected.items():
            assert getattr(employee, key) == val, \
                f"{GlobalErrorMessages.FIELD_MISMATCH.value}: '{key}' – ожидалось '{val}', получили '{getattr(employee, key)}'"

    with allure.step("✅ Сотрудник успешно создан"):
        msg = f"[OK] Sbb Employee создан: {employee.firstname} {employee.surname}"
        print(msg)
        allure.attach(msg, name="Sbb Employee", attachment_type=allure.attachment_type.TEXT)


@allure.title("Создание ментора")
def test_create_mentor(admin_token, employee_client, mentor_payload_template):
    payload = mentor_payload_template()
    expected = extract_expected_mentor_fields(payload)
    adapter = TypeAdapter(MentorCreateResponseSchema)

    with allure.step("Создаём ментора через /mentors"):
        res = employee_client.create_mentor(admin_token, payload)
        assert res.status_code == 200, \
            f"{GlobalErrorMessages.MENTOR_CREATION_FAILED.value}: {res.text}"
        mentor = adapter.validate_python(res.json())

    with allure.step("Проверяем ключевые поля ответа"):
        for key, val in expected.items():
            assert getattr(mentor, key) == val, \
                f"{GlobalErrorMessages.FIELD_MISMATCH.value}: '{key}' – ожидалось '{val}', получили '{getattr(mentor, key)}'"

    with allure.step("✅ Ментор успешно создан"):
        msg = f"[OK] Mentor создан: {mentor.firstname} {mentor.surname}"
        print(msg)
        allure.attach(msg, name="Mentor", attachment_type=allure.attachment_type.TEXT)
