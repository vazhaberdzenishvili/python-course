#Task 1
int_list = [10, 20, 30, 40]
def append_to_list(num):
  global int_list
  int_list.append(num)

append_to_list(16)
print(int_list)


#Task 2
def sum_nums(num):
  if num == 0:
    return 0
  else:
    return (num % 10) + sum_nums(num // 10)
  
sum_result = sum_nums(56)
print(f"Result: {sum_result}")


#Task 3
def reverse_txt(txt):
  if len(txt) <= 1:
    return txt
  else:
    return txt[-1] + reverse_txt(txt[:-1])
  
print(reverse_txt("code"))


#Task 4
def fibonacci_seq(n):
  if n <=0:
    return []
  elif n == 1:
    return [1]
  elif n == 2:
    return [1, 2]
  else:
    sequence = fibonacci_seq(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence
  
print(fibonacci_seq(8))