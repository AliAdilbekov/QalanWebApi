from src.utils.get_token import get_token

def test_get_token_success():
    token = get_token()
    assert token.startswith("ey"), "Получен некорректный токен"
    print(f"[SUCCESS] Токен получен: {token[:30]}...")
