"""Аутентификация пользователей."""

import hashlib

MAX_ATTEMPTS = 5


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def normalize_email(email):
    return email.strip().lower()


def authenticate(email, password, users, attempts=None):
    """Проверяет логин и пароль. users: {email: password_hash}."""
    key = normalize_email(email)
    if attempts is not None and attempts.get(key, 0) >= MAX_ATTEMPTS:
        raise PermissionError("too many login attempts")
    stored = users.get(key)
    if stored is None:
        return False
    return stored == hash_password(password)
