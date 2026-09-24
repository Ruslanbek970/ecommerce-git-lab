"""Новый сценарий оформления заказа (за фича-флагом)."""

NEW_CHECKOUT_ENABLED = False


def place_order(cart, customer):
    if not NEW_CHECKOUT_ENABLED:
        raise RuntimeError("new checkout flow is disabled")
    # TODO: интеграция с платёжным шлюзом не дописана
    return {"status": "draft", "items": cart, "customer": customer}
