from src.auth import authenticate, hash_password


USERS = {"aisha@shop.kz": hash_password("Qwerty12345")}


def test_login_success():
    assert authenticate("aisha@shop.kz", "Qwerty12345", USERS) is True


def test_login_wrong_password():
    assert authenticate("aisha@shop.kz", "wrong", USERS) is False


def test_unknown_user():
    assert authenticate("nobody@shop.kz", "Qwerty12345", USERS) is False


def test_too_many_attempts():
    import pytest

    from src.auth import MAX_ATTEMPTS

    attempts = {"aisha@shop.kz": MAX_ATTEMPTS}
    with pytest.raises(PermissionError):
        authenticate("aisha@shop.kz", "Qwerty12345", USERS, attempts)


def test_login_is_case_and_space_insensitive():
    """Регрессия на 68e722b: email нормализуется перед поиском пользователя."""
    assert authenticate("Aisha@Shop.KZ", "Qwerty12345", USERS) is True
    assert authenticate("  aisha@shop.kz  ", "Qwerty12345", USERS) is True
