"""Программа лояльности (в разработке, релиз v1.1)."""

POINTS_PER_TENGE = 0.01


def points_for_order(total):
    """Сколько бонусов начислить за заказ."""
    return int(total * POINTS_PER_TENGE)


def tier_for_customer(customer):
    # TODO: уровни silver/gold ещё не согласованы с маркетингом
    raise NotImplementedError("tier calculation is not ready yet")
