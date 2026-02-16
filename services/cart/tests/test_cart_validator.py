import pytest
from services.cart.validator import is_valid_item

@pytest.mark.unit
def test_valid_item():
    assert is_valid_item('apple')
