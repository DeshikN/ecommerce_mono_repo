import pytest
import time
import logging
from services.cart.service import add_item
from services.checkout.service import checkout
from services.order.service import create_order

logging.basicConfig(level=logging.INFO)

@pytest.mark.e2e
@pytest.mark.testrail("1510")
def test_e2e_checkout_success():
    logging.info("TestRail ID: 1510 - E2E checkout success started")

    cart = add_item([], 'apple')
    assert checkout(cart)
    assert create_order(cart)['status'] == 'CREATED'

    order = create_order(cart)
    assert order['status'] == 'CREATED'

    logging.info("TestRail ID: 1510 - E2E checkout success completed")


@pytest.mark.e2e
@pytest.mark.testrail("1511")
def test_e2e_checkout_multiple_items():
    logging.info("TestRail ID: 1511 - E2E checkout with multiple items started")

    cart = []
    cart = add_item(cart, 'apple')
    cart = add_item(cart, 'banana')

    assert checkout(cart)
    order = create_order(cart)
    assert len(order['items']) == 2

    logging.info("TestRail ID: 1511 - E2E checkout with multiple items completed")
