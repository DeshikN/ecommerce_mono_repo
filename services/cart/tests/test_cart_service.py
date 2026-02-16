import pytest
from services.cart.service import add_item

@pytest.mark.unit
def test_add_item():
    cart = []
    assert 'apple' in add_item(cart, 'apple')
