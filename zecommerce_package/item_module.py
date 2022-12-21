class Item:
    def __init__(self):
        self.id = None
        self.desc = None
        self.qty = None
        self.price = None
        print("Browser Launch!!!")

    def print_item_detail(self):
        print(self.id)
        print(self.desc)
        print(self.qty)
        print(self.price)
        print(15 * '*')

    def print_discounted_price(self):
        print(self.qty)
        print(self.price)
        if self.qty == 2:
            print("10%")
            final_price = (self.price-(self.price * 10 / 100))*self.qty
            print(final_price)
        elif 3 <= self.qty <= 5:
            print("15%")
            final_price = (self.price - (self.price * 15 / 100)) * self.qty
            print(final_price)
        elif self.qty > 5:
            final_price = (self.price - (self.price * 25 / 100)) * self.qty
            print(final_price)
            print("25%")
        else:
            print("Discount available only order with qty more than 1")
