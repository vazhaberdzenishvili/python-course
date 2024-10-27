# Task 1
num = int(input("Please enter the number: "))
if num % 2 == 0:
  print("the number is Even")
else:
  print("the number is Odd")


# Task 2
text = input("please enter a text: ")
if "small" in text:
  print("text")
elif "middle" in text:
   print("middle")
elif "tall" in text:
   print("tall")
else:
  print("Nothing found related to the word:", text)
  
#############
# if text == "small" or text == "tall" or text == "middle":
#   print(text)
# else:
#   print("Nothing found related to the word:", text)
######


# Task 3
num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))
operator=input("Please input the operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Attempt to divide by zero"
else:
    result = "Error: Invalid operator"

print("The result: ", result)