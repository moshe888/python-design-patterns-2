import pytest

from compositeANDdecoretor import *

@pytest.fixture()
def prodact():
    return Product("name",50)

@pytest.fixture()
def cart():
    iPhoneDeal = Bundle([
        Product('iPhone', 750),
        Product('iPhone case', 20),
        Bundle([
            Product('Support', 50),
            Product('Cool Apps', 20),
        ])
    ])
    discount = PercentDiscount(BuyXGetY(Discount(), 20, 10), 0.5)
    iPhoneDeal.add_discount(discount)

    return ShoppingCart([
        iPhoneDeal,
        Product('Galaxy', 550),
    ])


def test_product():
    p1 = Product("name", 50)
    assert p1.name == "name"
    assert p1.price == 50

    with pytest.raises(TypeError):
        Product(4, 4)



def test_discount(prodact):
    assert Discount().price_after_discount(prodact) == prodact.price


def test_precent_discounot(prodact):
    d = Discount()
    assert PercentDiscount(d, 0).price_after_discount(prodact) == prodact.price
    assert PercentDiscount(d, 0.1).price_after_discount(prodact) == prodact.price * 0.9
    assert PercentDiscount(d, 1).price_after_discount(prodact) == 0

def test_buyxgety_discount(prodact):
    d = Discount()
    assert BuyXGetY(d, 0,0).price_after_discount(prodact) == prodact.price
    p1 =  BuyXGetY(d, 40,20).price_after_discount(prodact)
    p2 = prodact.price
    if  p2 > 40:
        p2 -= 20
    assert  p1 == p2

def test_combination_discounts(prodact):
    p1 = PercentDiscount(BuyXGetY(Discount(), 40, 10), 0.5).price_after_discount(prodact)
    p2 = prodact.price
    if  p2 > 40:
        p2 -= 10
    p2 *= 0.5
    assert p1 == p2




def test_for_init_cart():
    # s1 = ShoppingCart([])
    # assert s1
    # p = Product('Galaxy', 550)
    # s2 = ShoppingCart([p])
    # assert s2 == None
    pass

def test_for_price(cart):
    assert cart.price() == 965.0, "Cart price is wrong"

def test_for_init_prodact():
    # p = Product("DD","DD")
    # assert p == None
    pass

@pytest.mark.parametrize(
    'discount, output',
    [
        (BuyXGetY(Discount(), 20, 10), 40),
        (BuyXGetY(Discount(), 20, 30),20 ),
        (PercentDiscount(Discount(),0.4), 30),
        (BuyXGetY(PercentDiscount(Discount(), 0.5),30,10), 25)

    ]
)

def test_for_add_discount(prodact,discount,output):
    prodact.add_discount(discount)
    assert prodact.price == output
range