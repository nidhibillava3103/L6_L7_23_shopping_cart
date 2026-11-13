
ZONES = {
    "1": "North",
    "2": "North",
    "3": "West",
    "4": "West",
    "5": "South",
    "6": "South",
    "7": "East",
    "8": "East"
}


# FIX 1: CART TOTAL

def cart_total(cart):

    if not isinstance(cart, str) or not cart.strip():
        return 0

    total = 0

    try:
        for item in cart.split(','):

            name, rest = item.split(':', 1)
            price, qty = rest.split('x', 1)

            if not name.strip():
                return 0

            price = int(price)
            qty = int(qty)

            if price < 0 or qty < 0:
                return 0

            total += price * qty

        return total

    except (ValueError, TypeError, AttributeError):
        return 0


# FIX 2: PROMO PERCENTAGE

def promo_percent(code):

    if not isinstance(code, str):
        return 0

    code = code.strip().upper()

    if not code.startswith("OFF"):
        return 0

    percentage = code[3:]

    if not percentage.isdigit():
        return 0

    percentage = int(percentage)

    if percentage < 0 or percentage > 100:
        return 0

    return percentage


# FIX 3: DELIVERY ZONE

def delivery_zone(pincode):

    if not isinstance(pincode, str):
        return "Unknown"

    if len(pincode) != 6 or not pincode.isdigit():
        return "Unknown"

    return ZONES.get(pincode[0], "Unknown")


def main():

    print("==== Running cart_total ====")

    user_input = input(
        "Enter cart as name:pricexqty CSV "
        "(e.g. pen:10x2,book:250x1): "
    )

    result = cart_total(user_input)
    print("Cart Total:", result)

    print("\n==== Running promo_percent ====")

    user_input = input("Enter a promo code (e.g. OFF20): ")

    result = promo_percent(user_input)
    print("Discount Percent:", result)

    print("\n==== Running delivery_zone ====")

    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")

    result = delivery_zone(user_input)
    print("Delivery Zone:", result)


if __name__ == "__main__":
    main()
