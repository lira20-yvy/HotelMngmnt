import pytest
from hotel import calculate_total, get_price_and_name, item_prices


def test_calculate_total():

    assert calculate_total(100, 2) == 200
    assert calculate_total(50, 4) == 200


def test_get_price_and_name():

    price, name = get_price_and_name(2, 1)
    assert price == item_prices['rooms'][0]
    assert name == "Room 1"

    price, name = get_price_and_name(3, 2)
    assert price == item_prices['packages'][1]
    assert name == "Package 2"

    price, name = get_price_and_name(4, 3)
    assert price == item_prices['foods'][2]
    assert name == "Food 3"


    price, name = get_price_and_name(5, 1)
    assert price == 0
    assert name == ""

