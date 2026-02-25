import pytest
import logging
from services.cart.service import add_item
from services.checkout.service import checkout

logging.basicConfig(level=logging.INFO)

@pytest.mark.integration
@pytest.mark.testrail("1411")
def test_cart_to_checkout_flow_failure():
    logging.info("TestRail ID: 1411 - Cart to checkout integration started")

    try:
        cart = add_item([], 'apple')

        # Simulate unexpected system failure
        raise RuntimeError("Checkout service unavailable")

        result = checkout(cart)

        assert result is True

    except Exception as e:
        logging.error(f"TestRail ID: 1411 - System failure occurred: {str(e)}")
        pytest.fail(f"Integration failed due to system error: {str(e)}")

    logging.info("TestRail ID: 1411 - Cart to checkout integration completed")


@pytest.mark.integration
@pytest.mark.testrail("1412")
def test_checkout_fails_with_empty_cart_system_issue():
    logging.info("TestRail ID: 1412 - Checkout with empty cart started")

    try:
        cart = []

        # Simulating unexpected crash in checkout service
        raise ConnectionError("Database connection lost during checkout")

        result = checkout(cart)
        assert result is False

    except Exception as e:
        logging.error(f"TestRail ID: 1412 - Critical failure: {str(e)}")
        pytest.fail(f"Checkout system failure: {str(e)}")

    logging.info("TestRail ID: 1412 - Checkout with empty cart completed")
