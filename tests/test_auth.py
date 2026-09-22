from src.auth import authenticate, hash_password


USERS = {"aisha@shop.kz": hash_password("Qwerty12345")}


def test_login_success():
    assert authenticate("aisha@shop.kz", "Qwerty12345", USERS) is True


def test_login_wrong_password():
    assert authenticate("aisha@shop.kz", "wrong", USERS) is False


def test_unknown_user():
    assert authenticate("nobody@shop.kz", "Qwerty12345", USERS) is False
