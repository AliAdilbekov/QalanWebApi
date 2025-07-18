import pytest
from api_clients.chat_client import ChatClient
from utils.get_token import get_mentor_token, get_pupil_token

@pytest.fixture
def mentor_token():
    return get_mentor_token()

@pytest.fixture
def pupil_token():
    return get_pupil_token()

@pytest.fixture
def chat_client():
    return ChatClient()

@pytest.fixture
def static_pupil_id():
    return 51
