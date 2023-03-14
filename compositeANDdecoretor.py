class Discount:
    def price_after_discount(self, product):
        return product.price


class PercentDiscount:
    def __init__(self, discount, pct):
        self.pct = pct
        self.discount = discount

    def price_after_discount(self, product):
        baseprice = self.discount.price_after_discount(product)
        return baseprice * (1 - self.pct)


class BuyXGetY:
    def __init__(self, discount, minprice, reduction):
        self.discount = discount
        self.minprice = minprice
        self.reduction = reduction

    def price_after_discount(self, product):
        baseprice = self.discount.price_after_discount(product)

        if baseprice > self.minprice:
            return baseprice - self.reduction
        else:
            return baseprice


class ShoppingCart:
    def __init__(self, products):
        self.products = products
        # for p in self.products:
        #     if not isinstance(p, Product):
        #         return None

    def price(self):
        return sum([x.price for x in self.products])


class Product:
    def __init__(self, name, price):
        if (type(name) is not str) or (type(price) is not int):
            raise TypeError()
        self.name = name
        self.price = price

    def add_discount(self, discount):
        self.price = discount.price_after_discount(self)


class Bundle:
    def __init__(self, products):
        self.price = sum([x.price for x in products])

    def add_discount(self, discount):
        self.price = discount.price_after_discount(self)


if __name__ == "__main__":
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

    s = ShoppingCart([
        iPhoneDeal,
        Product('Galaxy', 550),
    ])

    print(s.price())
