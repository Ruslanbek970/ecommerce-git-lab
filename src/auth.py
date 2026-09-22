"""Аутентификация пользователей."""

import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def normalize_email(email):
    return email.strip().lower()


def authenticate(email, password, users):
    """Проверяет логин и пароль. users: {email: password_hash}."""
    stored = users.get(normalize_email(email))
    if stored is None:
        return False
    return stored == hash_password(password)
