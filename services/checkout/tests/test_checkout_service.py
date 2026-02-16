import pytest
from services.checkout.service import checkout

@pytest.mark.unit
def test_checkout():
    assert checkout(['item'])
