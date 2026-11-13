
import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# ITEM TOTAL - BRANCH TESTS

def test_valid_food():
    assert item_total("food", 100, 2) == 210


def test_invalid_category():
    with pytest.raises(ValueError):
        item_total("toys", 100, 2)


def test_negative_price():
    with pytest.raises(ValueError):
        item_total("food", -100, 2)


def test_zero_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)


def test_bulk_quantity():
    assert item_total("food", 100, 10) == 945


def test_non_bulk_quantity():
    assert item_total("food", 100, 5) == 525


# CART DISCOUNT - BRANCH TESTS

def test_cart_above_5000():
    assert cart_discount(6000, False, None) == 500


def test_cart_between_2000_and_5000():
    assert cart_discount(3000, False, None) == 200


def test_cart_below_2000():
    assert cart_discount(500, False, None) == 0


def test_prime_member():
    assert cart_discount(500, True, None) == 100


def test_non_prime_member():
    assert cart_discount(500, False, None) == 0


def test_valid_coupon():
    assert cart_discount(1000, False, "FLAT10") == 100


def test_invalid_coupon():
    assert cart_discount(1000, False, "SAVE10") == 0


def test_coupon_below_minimum_value():
    assert cart_discount(500, False, "FLAT10") == 0


# SHIPPING FEE - BRANCH TESTS

def test_prime_standard_shipping():
    assert shipping_fee(100, True, False) == 0


def test_non_prime_high_value_shipping():
    assert shipping_fee(500, False, False) == 0


def test_non_prime_low_value_shipping():
    assert shipping_fee(100, False, False) == 40


def test_express_non_prime():
    assert shipping_fee(100, False, True) == 140


def test_express_prime():
    assert shipping_fee(100, True, True) == 50


def test_standard_prime_shipping():
    assert shipping_fee(1000, True, False) == 0
