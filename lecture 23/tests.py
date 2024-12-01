import unittest
import shoppingCart, bank


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = shoppingCart.ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Keyboard", 39.99, 1)
        item = self.cart.items[0]
        self.assertEqual((item['name'], item['price'], item['quantity']), ("Keyboard", 39.99, 1))

        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Mouse", 9.99, 0)

        self.assertEqual(str(context.exception), "Quantity must be greater than 0")

        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Mouse", 9.99, -5)

        self.assertEqual(str(context.exception), "Quantity must be greater than 0")

    def test_total_price(self):
        self.cart.add_item("Keyboard", 39.99, 1)
        self.cart.add_item("Mouse", 10.00, 2)
        self.assertEqual(self.cart.total_price(), 59.99)

    def test_remove_item(self):
        self.cart.add_item("Keyboard", 39.99, 1)
        self.cart.add_item("Mouse", 10.00, 2)
        self.cart.remove_item("Mouse")
        self.assertEqual(self.cart.items, [{'name': 'Keyboard', 'price': 39.99, 'quantity': 1}])

    def test_is_empty(self):
        self.cart.add_item("Keyboard", 39.99, 1)
        self.assertEqual(self.cart.is_empty(), False)


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = bank.BankAccount("Michael Williams", 2500)

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 3500)

        with self.assertRaises(ValueError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

        with self.assertRaises(ValueError) as context:
            self.account.deposit(-600)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

    def test_withdraw(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 1500)

        with self.assertRaises(ValueError) as context:
            self.account.withdraw(2600)
        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 2500)


if __name__ == '__main__':
    unittest.main()
