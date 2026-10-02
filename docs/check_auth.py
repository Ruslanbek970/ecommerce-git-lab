"""Тест для git bisect: работает ли вход, если email введён не в нижнем регистре.
exit 0 — коммит хороший, exit 1 — плохой. Лежит вне репозитория, чтобы
bisect мог запускать один и тот же тест на любом коммите."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.cwd()))
from src.auth import authenticate, hash_password  # noqa: E402

users = {"aisha@shop.kz": hash_password("Qwerty12345")}
ok = (
    authenticate("aisha@shop.kz", "Qwerty12345", users) is True
    and authenticate("Aisha@Shop.KZ", "Qwerty12345", users) is True
    and authenticate("  aisha@shop.kz  ", "Qwerty12345", users) is True
)
print("GOOD" if ok else "BAD")
sys.exit(0 if ok else 1)
