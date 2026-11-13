
import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# TEST CASES FOR ITEM TOTAL

def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_electronics_item():
    assert item_total("electronics", 100, 1) == 118


def test_clothing_item():
    assert item_total("clothing", 100, 1) == 112


def test_bulk_discount():
    assert item_total("food", 100, 10) == 945


def test_invalid_category():
    with pytest.raises(ValueError):
        item_total("toys", 100, 2)


def test_invalid_price():
    with pytest.raises(ValueError):
        item_total("food", -100, 2)


def test_invalid_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)


# TEST CASES FOR CART DISCOUNT

def test_high_cart_discount():
    assert cart_discount(6000, False, None) == 500


def test_medium_cart_discount():
    assert cart_discount(3000, False, None) == 200


def test_no_cart_discount():
    assert cart_discount(500, False, None) == 0


def test_prime_discount():
    assert cart_discount(500, True, None) == 100


def test_coupon_discount():
    assert cart_discount(1000, False, "FLAT10") == 100


# TEST CASES FOR SHIPPING FEE

def test_prime_free_shipping():
    assert shipping_fee(100, True, False) == 0


def test_non_prime_free_shipping():
    assert shipping_fee(500, False, False) == 0


def test_paid_shipping():
    assert shipping_fee(100, False, False) == 40


def test_express_shipping():
    assert shipping_fee(100, False, True) == 140


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50
