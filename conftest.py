from tests.fixtures.auth_register_fixtures import *
from tests.fixtures.auth_login_fixtures import *
from tests.fixtures.subscriptions_fixtures import *
from tests.fixtures.employees_fixtures import *
from tests.fixtures.chat_fixtures import *
import pytest
from src.utils.telegram_alert import send_telegram_message 


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        test_name = item.name
        nodeid = item.nodeid
        error_msg = str(result.longrepr)

        message = (
            f"❌ *Упал тест:*\n"
            f"`{nodeid}`\n\n"
            f"*Ошибка:*\n"
            f"```{error_msg[:4000]}```"
        )

        send_telegram_message(message)

