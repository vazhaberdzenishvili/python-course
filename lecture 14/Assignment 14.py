#Task 1
class BankAccount:
  def __init__(self, account_number, account_holder, balance):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = balance

  def deposit_money(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"{amount}₾ has been successfully deposited into the account")
    else:
      print("Invalid amount") 

  def withdraw(self, amount):
    if amount <= 0:
      print("Invalid amount")
    elif amount > self.balance:
      print("Insufficient money")
    else:
      self.balance -= amount
      print(f"{amount}₾ has been successfully withdrawn from the account")

  def check_balance(self):
    print(f"Balance: {self.balance}₾")

account1 = BankAccount("10506", "Michael", 400)
account2 = BankAccount("10507", "James", 550)

account1.deposit_money(900)
account1.withdraw(1100)
account1.check_balance()

account2.deposit_money(500)
account2.withdraw(1100)
account2.check_balance()

#Task 2
class Student:
  def __init__(self, name, student_id):
    self.name = name
    self.student_id = student_id
    self.courses = []

  def add_course(self, course):
    if course not in self.courses:
      self.courses.append(course)
      print(f"{self.name} has successfully enrolled in {course}")
    else:
      print(f"{self.name} is already enrolled in the {course}")

  def show_info(self):
    print(f"Student Name: {self.name}")
    print(f"Student ID: {self.student_id}")

  def show_courses(self):
    if self.courses:
      print(f"Enrolled Courses: {', '.join(self.courses)}")
    else:
      print(f"No courses to show for {self.name}")

student1 = Student("Michael Williams", "0001")
student2 = Student("Daniel Richards", "0002")

student1.add_course("Biology")
student1.add_course("Chemistry")
student1.show_info()
student1.show_courses()

student2.add_course("History")
student2.add_course("Math")
student2.show_info()
student2.show_courses()