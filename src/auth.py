"""Аутентификация пользователей."""

import configparser
import hashlib
import pathlib

CONFIG_PATH = pathlib.Path(__file__).resolve().parent.parent / "config" / "security.conf"


def _max_attempts():
    parser = configparser.ConfigParser()
    parser.read(CONFIG_PATH)
    return parser.getint("password_policy", "max_login_attempts", fallback=5)


MAX_ATTEMPTS = _max_attempts()


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
