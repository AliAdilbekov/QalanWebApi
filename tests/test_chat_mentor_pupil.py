import pytest
import allure
from typing import List
from pydantic import TypeAdapter

from src.schemas.chat_schemas import ChatMessageSchema
from src.utils.data_generator import (
    generate_unique_chat_message_mentor,
    generate_unique_chat_message_pupil,
)
from src.utils.helpers import message_exists
from src.enums.global_enums import GlobalErrorMessages


@allure.title("Ментор и ученик обмениваются сообщениями")
def test_chat_bidirectional(mentor_token, pupil_token, chat_client, static_pupil_id):
    mentor_msg = generate_unique_chat_message_mentor()
    pupil_msg = generate_unique_chat_message_pupil()
    adapter = TypeAdapter(List[ChatMessageSchema]) 

    with allure.step(f"Ментор отправляет сообщение: {mentor_msg}"):
        res = chat_client.send_message(mentor_token, static_pupil_id, mentor_msg)
        assert res.status_code == 200
        assert res.json().get("status") == "ok"

    with allure.step("Ученик получает сообщение от ментора"):
        res = chat_client.get_messages(pupil_token)
        assert res.status_code == 200
        messages = adapter.validate_python(res.json())
        assert message_exists(messages, mentor_msg), \
            f"{GlobalErrorMessages.PUPIL_DID_NOT_RECEIVE_MESSAGE.value}: '{mentor_msg}'"

    with allure.step(f"Ученик отправляет сообщение: {pupil_msg}"):
        res = chat_client.send_message(pupil_token, static_pupil_id, pupil_msg)
        assert res.status_code == 200
        assert res.json().get("status") == "ok"

    with allure.step("Ментор получает последнее сообщение ученика"):
        res = chat_client.get_last_messages_for_mentor(mentor_token, static_pupil_id)
        assert res.status_code == 200
        messages = adapter.validate_python(res.json().get("messages", []))
        assert message_exists(messages, pupil_msg), \
            f"{GlobalErrorMessages.MENTOR_DID_NOT_RECEIVE_MESSAGE.value}: '{pupil_msg}'"

    with allure.step("✅ Обмен сообщениями успешен"):
        msg = f"[OK] Ментор: {mentor_msg} | Ученик: {pupil_msg}"
        print(msg)
        allure.attach(msg, name="Обмен сообщениями", attachment_type=allure.attachment_type.TEXT)
