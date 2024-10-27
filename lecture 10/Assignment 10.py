#Task 1
def zip_lists(list1, list2):
  zipped = list(zip(list1, list2))
  return zipped

print(zip_lists([1, 2, 3], ['a', 'b', 'c']))

#Task 2
params = [1, 2, 3, 4, 5, 6, 7]
even_nums = list(filter(lambda x: x % 2 == 0, params))  

print(even_nums)

#Task 3
nums = [-2, -1, 0, 1, 2]
filtered_nums = list(filter(lambda x: x > 0, nums))

print(filtered_nums)

#Task 4
strings = ["level", "fix", "stats", "code", "radar"]

palindrome = list(filter(lambda c: c == c[::-1], strings))

#Taks 5
from functools import reduce

def multiplication(nums):
    try:
      return reduce(lambda x, y: x * y, nums)
    except TypeError:
      return "Elements must be numbers"
    
params = [None, 2, 3, 4, 5]
result = multiplication(params)

print(result)

#Task 6
def filter_strings(params, ending):
    try:
        return list(filter(lambda c: c.endswith(ending), params))
    except TypeError:
        return "Incorrect type of parameters"

params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
output = filter_strings(params, ending)

print(output)