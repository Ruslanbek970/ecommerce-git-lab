"""Расчёт стоимости доставки."""

BASE_COST = 800      # базовая стоимость, ₸
PER_KG = 150         # за каждый килограмм, ₸

ZONE_MULTIPLIER = {"almaty": 1.0, "regions": 1.4, "remote": 1.8}


def shipping_cost(weight_kg, zone="almaty"):
    """Стоимость доставки заказа весом weight_kg в зону zone.

    Зона по умолчанию — almaty, поэтому старые вызовы shipping_cost(weight)
    из feature-A продолжают работать.
    """
    if weight_kg < 0:
        raise ValueError("weight must not be negative")
    if zone not in ZONE_MULTIPLIER:
        raise ValueError(f"unknown zone: {zone}")
    return (BASE_COST + PER_KG * weight_kg) * ZONE_MULTIPLIER[zone]
