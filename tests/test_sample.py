import pytest
import logging
from services.cart.service import add_item
from services.checkout.service import checkout

logging.basicConfig(level=logging.INFO)

@pytest.mark.integration
@pytest.mark.testrail("1411")
def test_cart_to_checkout_flow_should_fail():
    logging.info("TestRail ID: 1411 - Cart to checkout integration started")

    # Add item to cart
    cart = add_item([], 'apple')

    # Intentionally wrong expected result to force failure
    # Assuming checkout should return True for valid cart
    result = checkout(cart)

    assert result is False, "Expected checkout to fail, but it passed"

    logging.info("TestRail ID: 1411 - Cart to checkout integration completed")


@pytest.mark.integration
@pytest.mark.testrail("1412")
def test_checkout_fails_with_empty_cart_should_fail():
    logging.info("TestRail ID: 1412 - Checkout with empty cart started")

    cart = []

    # Assuming checkout should return False for empty cart
    result = checkout(cart)

    # Intentionally incorrect assertion to create failure
    assert result is True, "Expected checkout to pass, but it failed"

    logging.info("TestRail ID: 1412 - Checkout with empty cart completed")
