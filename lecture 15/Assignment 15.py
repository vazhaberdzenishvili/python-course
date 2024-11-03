class Person:
  def __init__(self, name, deposit=1000, loan=0):
    self.name = name
    self.deposit = deposit
    self.loan = loan

  def __str__(self):
    return f"person:{self.name}, deposit:{self.deposit}, loan:{self.loan}"


class House:
  def __init__(self, ID, price, owner):
    self.ID = ID
    self.price = price
    self.owner = owner
    self.status = "for sale"

  def sale(self, buyer, loan=None):
    if loan is None:
      if buyer.deposit >= self.price:
        buyer.deposit -= self.price 
        self.owner.deposit += self.price 
        self.owner = buyer 
        self.status = "sold"
        return f"{buyer.name} has successfully purchased the house with the ID: {self.ID} for {self.price}, status: {self.status}"
      else:
        return f'{buyer.name}, not enough money to purchase the house. Deposit: {buyer.deposit}'
    else:
      total_amount = buyer.deposit + loan
      if total_amount >= self.price:
        buyer.loan += loan
        self.owner.deposit = 0
        self.owner = buyer
        self.status = "sold with a loan"
        return f"{buyer.name} has successfully purchased the house with the ID: {self.ID} for {self.price}, status: {self.status}"
      else:
        return f"{buyer.name}, total amount of money (loan + deposit): {total_amount} isn't enough to purchase the house."

owner = Person("Michael", deposit=12000)
buyer = Person("Alex", deposit=18000)

apartment = House(ID="001", price=18000, owner=owner)

print(owner)
print(buyer)

#without a loan
sale_notification = apartment.sale(buyer)
print(sale_notification)

#with a loan
buyer.deposit = 10000
sale_notification = apartment.sale(buyer,8000)
print(sale_notification)

#check buyer's status after the purchase
print(apartment.owner)

#ensure original owner (Michael) has updated deposit
print(owner)