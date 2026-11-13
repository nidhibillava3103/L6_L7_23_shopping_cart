
from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone


# FUZZ TEST 1: CART TOTAL

@given(st.one_of(st.text(), st.none()))
def test_cart_total_no_crash(s):
    try:
        cart_total(s)
    except Exception as e:
        assert False, f"cart_total crashed with input {s!r}: {e}"


# FUZZ TEST 2: PROMO PERCENTAGE

@given(st.one_of(st.text(), st.none()))
def test_promo_percent_no_crash(s):
    try:
        promo_percent(s)
    except Exception as e:
        assert False, f"promo_percent crashed with input {s!r}: {e}"


# FUZZ TEST 3: DELIVERY ZONE

@given(st.one_of(st.text(), st.none()))
def test_delivery_zone_no_crash(s):
    try:
        delivery_zone(s)
    except Exception as e:
        assert False, f"delivery_zone crashed with input {s!r}: {e}"
