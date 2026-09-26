"""Проверка требований Dev A: длина пароля и обязательные цифры."""
import configparser
import pathlib

CONFIG = pathlib.Path(__file__).resolve().parent.parent / "config" / "security.conf"


def policy():
    parser = configparser.ConfigParser()
    parser.read(CONFIG)
    return parser["password_policy"]


def test_minimum_length_is_at_least_12():
    assert policy().getint("minimum_password_length") >= 12


def test_numbers_required():
    assert policy().getboolean("require_numbers") is True
