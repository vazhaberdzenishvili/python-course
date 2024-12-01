class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]

    def is_empty(self):
        return len(self.items) == 0