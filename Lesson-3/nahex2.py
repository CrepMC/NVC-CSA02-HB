class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


class Order:
    def __init__(self, customer_id):
        self.item_list = []
        self.customer_id = customer_id

    def add_item(self, item):
        self.item_list.append(item)

    def total(self):
        return sum(item.total_price() for item in self.item_list)


class Promo:
    def discount(self, order):
        return 0


class BulkOrderPromo(Promo):
    def discount(self, order):
        discount = 0
        for item in order.item_list:
            if item.quantity > 10:
                discount += item.total_price() * 0.2  # 20% discount for bulk orders
        return discount


class LoyaltyPromo(Promo):
    def discount(self, order):
        # Assuming customer_id is used to determine loyalty
        # For simplicity, let's say customer_id < 1000 are loyal customers
        if order.customer_id < 1000:
            return order.total() * 0.05  # 5% discount for loyal customers
        return 0

# Example usage
items = []
try:
    while True:
        quantity = int(input("Enter quantity for item: "))
        price = float(input("Enter price for item: $"))
        item = Item(quantity=quantity, price=price)
        items.append(item)
except KeyboardInterrupt:
    print("\nFinished adding items.")

customer_id = int(input("Enter customer ID: "))
order = Order(customer_id=customer_id)
order.add_item(item)

bulk_promo = BulkOrderPromo()
loyalty_promo = LoyaltyPromo()

total_price = order.total()
bulk_discount = bulk_promo.discount(order)
loyalty_discount = loyalty_promo.discount(order)

final_price = total_price - bulk_discount - loyalty_discount

print(f"Total Price: ${total_price}")
print(f"Bulk Discount: ${bulk_discount}")
print(f"Loyalty Discount: ${loyalty_discount}")
print(f"Final Price: ${final_price}")
