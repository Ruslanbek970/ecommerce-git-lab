# ShopKZ — учебное e-commerce приложение

Маленькое приложение-корзина, которое используется как полигон для лабораторной
работы по Advanced Git & GitHub (DevOps 2, вариант A).

## Структура

```
src/
  payment.py   расчёт итоговой суммы заказа (скидка, НДС)
  auth.py      аутентификация пользователей
tests/
  test_payment.py
  test_auth.py
config/
  security.conf   политика паролей
.github/workflows/
  test.yml     CI: build, test, lint, security scan
```

## Запуск

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
```

## Ветки

| Ветка | Назначение |
|---|---|
| `main` | продакшн, только через Pull Request |
| `develop` | интеграционная ветка, новые фичи |
| `feature/*` | работа над отдельной задачей |
| `hotfix/*` | срочные правки продакшна, создаются от `main` |

Полный разбор задач лабораторной — в [REPORT.md](REPORT.md).

## Доставка

`shipping_cost(weight_kg)` считает стоимость доставки: базовые 800 ₸ плюс 150 ₸
за каждый килограмм. Отрицательный вес отклоняется с `ValueError`.

## Roadmap v1.1 (в работе в `develop`)

- [ ] программа лояльности и уровни клиентов
- [ ] новый сценарий оформления заказа
- [ ] вход через OAuth
