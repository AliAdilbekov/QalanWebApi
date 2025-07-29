from src.enums.global_enums import GlobalErrorMessages


def message_exists(messages, expected_text):
    return any(m.text == expected_text for m in messages)

def extract_expected_employee_fields(payload: dict) -> dict:
    return {
        "firstname": payload["firstname"],
        "surname": payload["surname"],
        "phoneNumber": payload["phoneNumber"],
        "role": payload["role"],
        "department": payload["department"],
    }


def extract_expected_mentor_fields(payload: dict) -> dict:
    return {
        "firstname": payload["firstname"],
        "surname": payload["surname"],
        "phoneNumber": payload["phoneNumber"],
        "qualification": payload["qualification"],
        "department": payload["department"],
    }


def validate_personal_study_pupil(pupil, expected: dict):
    assert pupil.fullname == expected["fullname"], GlobalErrorMessages.INVALID_NAME.value
    assert pupil.phoneNumber == expected["phone"], GlobalErrorMessages.INVALID_PHONE.value
    assert pupil.userId == expected["user_id"], GlobalErrorMessages.INVALID_USER_ID.value
    assert expected["subscription"] in pupil.allSubscriptionTypes, \
        GlobalErrorMessages.SUBSCRIPTION_NOT_FOUND.value.format(subscription=expected["subscription"])