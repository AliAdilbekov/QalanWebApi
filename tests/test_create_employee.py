import pytest
import allure
from utils.get_token import get_employee_token


@pytest.mark.parametrize("role", ["sbb_employee", "mentor"])
@allure.title("Создание сотрудника с ролью: {role}")
def test_create_employee_or_mentor(
    admin_token,
    employee_client,
    employee_payload_template,
    mentor_payload_template,
    role
):
    if role == "sbb_employee":
        with allure.step("Генерируем payload для обычного сотрудника"):
            payload = employee_payload_template(role=role)
            expected_fields = {
                "firstname": payload["firstname"],
                "surname": payload["surname"],
                "phoneNumber": payload["phoneNumber"],
                "role": role,
                "department": payload["department"],
            }

        with allure.step("Создаём сотрудника через /employees"):
            response = employee_client.create_employee(admin_token, payload)
            assert response.status_code == 200, f"❌ Ошибка: {response.text}"
            data = response.json()

    elif role == "mentor":
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
            assert response.status_code == 200, f"❌ Ошибка: {response.text}"
            data = response.json()

    with allure.step("Проверяем, что данные совпадают"):
        for key, val in expected_fields.items():
            assert data[key] == val, f"❌ {key} не совпадает: ожидалось {val}, получили {data.get(key)}"

    with allure.step("Готово"):
        msg = f"[OK] {role.title()} создан: {expected_fields['firstname']} {expected_fields['surname']}"
        print(msg)
        allure.attach(msg, name=f"{role.title()} создан", attachment_type=allure.attachment_type.TEXT)


