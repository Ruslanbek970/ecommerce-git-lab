from src.payment import installment_plan, promo_discount


def test_installment_plan():
    assert installment_plan(12000, 12) == 1000.0


def test_installment_rejects_zero_months():
    import pytest

    with pytest.raises(ValueError):
        installment_plan(1000, 0)


def test_promo_discount_is_capped_by_subtotal():
    assert promo_discount("WELCOME1000", 400) == 400
    assert promo_discount("UNKNOWN", 5000) == 0
