import pytest
from project import calculate_total, update_stock, get_price_and_name

@pytest.fixture
def sample_stock():
    return {
        'rooms': [3, 3, 3, 2],
        'packages': [3, 2, 2, 2],
        'foods': [3, 3, 2, 2],
    }

def test_calculate_total():
    assert calculate_total(1999, 2) == 3998
    assert calculate_total(0, 5) == 0

def test_update_stock_success(sample_stock):
    result = update_stock(sample_stock, 'rooms', 1, 2)
    assert result is True
    assert sample_stock['rooms'][0] == 1

def test_update_stock_failure(sample_stock):
    result = update_stock(sample_stock, 'rooms', 1, 5)
    assert result is False
    assert sample_stock['rooms'][0] == 3

def test_get_price_and_name():
    price, name = get_price_and_name(2, 1)
    assert price == 1999
    assert name == "Room 1"

def test_get_price_and_name_invalid():
    price, name = get_price_and_name(99, 1)
    assert price == 0
    assert name == ""
