from enum import Enum

class GlobalErrorMessages(Enum):
    CREATE_PUPIL_FAILED = "❌ Ошибка создания ученика:"
    RETRY_FAIL = "❌ Ошибка подписки:"
    FREEZING_ALREADY_EXISTS = "⚠️ Заморозка уже существует на дату"
    FREEZING_FAILED = "❌ Ошибка при заморозке:"
    FREEZING_DATE_MISMATCH = "❌ Дата заморозки не совпадает:"
    PUPIL_DID_NOT_RECEIVE_MESSAGE = "❌ Ученик не получил сообщение"
    MENTOR_DID_NOT_RECEIVE_MESSAGE = "❌ Ментор не получил сообщение от ученика"
    EMPLOYEE_CREATION_FAILED = "❌ Ошибка создания сотрудника:"
    MENTOR_CREATION_FAILED = "❌ Ошибка создания ментора:"
    FIELD_MISMATCH = "❌ Поле не совпадает"
    USER_ID_NOT_FOUND = "❌ userId не найден"