import pytest
from services.order.service import create_order

@pytest.mark.unit
def test_order():
    assert create_order(['x'])['status'] == 'CREATED'
