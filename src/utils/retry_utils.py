from tenacity import retry, stop_after_attempt, wait_fixed, before_sleep_log
import logging
import allure

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

def retry_on_failure(max_attempts=3, wait_seconds=2):
    def decorator(func):
        @retry(
            stop=stop_after_attempt(max_attempts),
            wait=wait_fixed(wait_seconds),
            reraise=True,
            before_sleep=before_sleep_log(logger, logging.INFO)
        )
        def wrapper(*args, **kwargs):
            attempt_number = wrapper.retry.statistics.get("attempt_number", 1)
            with allure.step(f"🔁 Попытка #{attempt_number} вызова: {func.__name__}"):
                logger.info(f"▶️ Попытка #{attempt_number} вызова {func.__name__}")
                return func(*args, **kwargs)
        return wrapper
    return decorator
