# Task 1
mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
result = mylist[2] + mylist[8] + mylist[13]
print("The result it: ", result)

# Task 2
import random

random_list=[]
for _ in range(20):
  random_list.append(random.randint(1, 100))
print("Random list: ", random_list)

odd_numbers = []
for num in random_list:
  if num % 2 != 0:
    odd_numbers.append(num)

odd_numbers.sort()
print("Odd numbers: ", odd_numbers)

if odd_numbers:
  smallest_num = odd_numbers[0]
  largest_num = odd_numbers[-1]
  print('Smallest number is {}, largest number is {}'.format(smallest_num,largest_num))
else:
  print("The list is empty")


# Task 3
#a
my_llist = [43, '22', 12, 66, 210, ["hi"]]
print("Index of 210: ", my_llist.index(210))
#b
my_llist[5].append("hello")
#c
my_llist.pop(2)
print("the list after removing the number with index 2: ", my_llist)
#d
my_llist_2 = my_llist.copy()
my_llist_2.clear()
print("my_llist:", my_llist)
print("my_llist_2:", my_llist_2)

# Task 4
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [1, 6, 5],
    [3, 0, 2],
    [2, 1, 0]
]

sum_result = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    sum_result.append(row)
for row in sum_result:
    print(row)

# Task 5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = []

for j in range(3):
    transposed_row = []
    for i in range(3):
        transposed_row.append(matrix[i][j])
    transposed_matrix.append(transposed_row)    
print("Transposed matrix: ")
for row in transposed_matrix:
  print(row)


# Task 6
import random

matrix = [[random.randint(1, 100)] * 4 for _ in range(4)]
print("4x4 matrix: ")
for row in matrix:
    print(row)
