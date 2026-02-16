import pytest
from services.payment.retry_policy import retry_count

@pytest.mark.unit
def test_retry():
    assert retry_count(1) == 2
