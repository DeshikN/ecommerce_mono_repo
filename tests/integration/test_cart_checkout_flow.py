import pytest
import logging
from services.cart.service import add_item
from services.checkout.service import checkout

logging.basicConfig(level=logging.INFO)

@pytest.mark.integration
@pytest.mark.testrail("1512")
def test_cart_to_checkout_flow():
    logging.info("TestRail ID: 1512 - Cart to checkout integration started")

    cart = add_item([], 'apple')
    assert checkout(cart)

    logging.info("TestRail ID: 1512 - Cart to checkout integration completed")


@pytest.mark.integration
@pytest.mark.testrail("1513")
def test_checkout_fails_with_empty_cart():
    logging.info("TestRail ID: 1513 - Checkout with empty cart started")

    cart = []
    assert checkout(cart) is False

    logging.info("TestRail ID: 1513 - Checkout with empty cart completed")
