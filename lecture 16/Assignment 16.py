#Task 1
def NumChecker(func):
  def wrapper(number):
    if number < 0:
      raise ValueError("Provided number isn't positive")  
    else:
      return func(number)
  return wrapper

@NumChecker
def return_num(num):
  return num

print(return_num(20))
try:
  return_num(-10)
except ValueError as e:
  print(e) 

#Task 2
class NumChecker:
  def __init__(self, func):
    self.func = func 

  def __call__(self, num):
    if num < 0:
      raise ValueError("Provided number isn't positive")       
    return num 

@NumChecker
def return_num(num):
  return num

print(return_num(10))
try:
  print(return_num(-20))
except ValueError as e:
  print(e)

#Task 3
import time

def calculate_duration(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    res = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time of {func.__name__} is {execution_time} seconds")
    return res
  return wrapper

@calculate_duration
def sum_of_range(n):
  return n ** n

sum_of_range(123456)

#Task 4
class LoggingMeta(type):
  def __new__(cls, name, bases, dct):
    print(f"Class {name} is being created")
    methods = [func for func in dct if callable(dct[func]) and not func.startswith('__')]
    print(f"Methods: {methods}")
    instance = super().__new__(cls, name, bases, dct)
    return instance

class RandomClass(metaclass=LoggingMeta):
  def method_one(self):
    pass
    
  def method_two(self):
    pass

test = RandomClass()