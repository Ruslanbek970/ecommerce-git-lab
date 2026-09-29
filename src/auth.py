"""Аутентификация пользователей."""

import hashlib

MAX_ATTEMPTS = 5


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def normalize_email(email):
    return email.strip().lower()


def find_user(email, users):
    """Ищет пользователя по email."""
    return users.get(email)


def authenticate(email, password, users, attempts=None):
    """Проверяет логин и пароль. users: {email: password_hash}."""
    if attempts is not None and attempts.get(email, 0) >= MAX_ATTEMPTS:
        raise PermissionError("too many login attempts")
    stored = find_user(email, users)
    if stored is None:
        return False
    return stored == hash_password(password)
