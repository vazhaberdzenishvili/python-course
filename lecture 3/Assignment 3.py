# Task 1
num = int(input("Enter the number: "))

if num < 1:
  print("The entered number should be greater than 0")
else:
  while num > 0:
    print(num)
    num-=1


# Task 2
user_input = input("Enter the number or sum: ")
total_sum = 0

while user_input != "sum":
  if user_input.isdigit():
    if int(user_input) > 0:
      total_sum += int(user_input)
    elif int(user_input) < 1:
      print("enter the number which is greater than 0")
    
  else:
     print("Please enter a valid number")    
  user_input = input("Enter the number or 'sum' to finish: ") 
if user_input.lower() == "sum":
  print("sum of the positive numbers is: ", total_sum)



# Task 3
import random

minimum_value = int(input("Enter the minimum value of the range"))
maximum_value = int(input("Enter the maximum value of the range"))             
target_num = random.randint(minimum_value, maximum_value)
lives = 3
inputted_num = int(input("Enter your guess: "))

while lives > 0:
    if inputted_num == target_num:
        print("Congratulations, you got it")
        break
    elif inputted_num > target_num:
        lives -= 1
        print("Your guess is higher than target number")
    elif inputted_num < target_num:
        lives -= 1
        print("Your guess is lower than target number")

    if lives > 0:
        print(lives, "lives left")
        inputted_num = int(input("Enter the number: "))
    else:
        print("Out of lives!")