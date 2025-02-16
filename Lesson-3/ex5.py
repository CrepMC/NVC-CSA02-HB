class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    
class Order:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.item_list:list[Item] = []
    def calc_total(self):
        total = 0
        for item in self.item_list:
            total += item.price * item.quantity
        return total

class Promo:
    def __init__(self, price):
        self.price = price
    def discount(self, percent):
        return self.price * percent / 100

order = Order(123)
item1 = Item(10, 500)
item2 = Item(3, 800)
order.item_list.append(item1)
order.item_list.append(item2)

promo = Promo(order.calc_total())
discounted_price = promo.discount(10)

print(f"Customer ID: {order.customer_id}")
print(f"Total price: {order.calc_total()}")
print(f"Discounted price: {discounted_price}")
print(f"Finally: {order.calc_total() - discounted_price}")
