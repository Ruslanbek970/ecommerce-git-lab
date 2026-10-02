"""Проверка требований Dev B: длинный пароль и обязательные спецсимволы."""
import configparser
import pathlib

CONFIG = pathlib.Path(__file__).resolve().parent.parent / "config" / "security.conf"


def policy():
    parser = configparser.ConfigParser()
    parser.read(CONFIG)
    return parser["password_policy"]


def test_minimum_length_is_16():
    assert policy().getint("minimum_password_length") == 16


def test_symbols_required():
    assert policy().getboolean("require_symbols") is True
