import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_canCalculateCurrentTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateCurrentTotal() == 1


def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateCurrentTotal() == 3


def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a",3,2)


def test_canApplyDiscountRule(checkout):
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addDiscount("a", 3, 2)
    assert  checkout.calculateCurrentTotal() == 2

def test_canThrowException(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")