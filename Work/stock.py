from typedproperty import String, Integer, Float

class Stock:
    __slots__ = ('_name','_shares','_price')

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price
    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, no_shares):
        self.shares -= no_shares
    
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
