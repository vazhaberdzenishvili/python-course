# Task 1
squared_numbers = {i**2 for i in range(1,10)}
print(squared_numbers)


#Task 2
inputted_str=(input("Enter a string: "))
symbols= set(inputted_str)
print("Symbols: ",symbols)


#Task 3
tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)
combined_tuple = tuple(set(tuple1 + tuple2))
duplicated_values = [num for num in combined_tuple if num in tuple1 and num in tuple2]
print("combined_tuple: ", combined_tuple)
print("duplicated_values: ", duplicated_values)


#Task 4
ordered_tuple = (1, 2, 3, 4)
swapped_tuple = (ordered_tuple[-1], ordered_tuple[1], ordered_tuple[2], ordered_tuple[0])
print("Modified version: ", swapped_tuple)


#Task 5
nested_tuple=(1, (2, 3), (4, (5, 6)))
items = []
for item in nested_tuple:
    if type(item) == tuple:
      for value in item:
        if type(value) == tuple:
            items.extend(value)
        else:
          items.append(value)
    else:
      items.append(item)
result = tuple(items)
print("Result: ", result)


#Task 6
set1 = {1, 2}
set2 = {'a', 'b'}
result = {(i, j) for i in set1 for j in set2}
print("Result: ", result)