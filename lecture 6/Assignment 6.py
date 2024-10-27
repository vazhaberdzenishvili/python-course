# Task 1
inputted_txt=str(input("Enter a sentence: "))
words = inputted_txt.split()
dct={}
for word in words:
  word = word.lower()
  if word in dct:
    dct[word] += 1
  else:
    dct[word] = 1
print(dct)


# Task 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter a mathematical operator: ")

operations = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Error: Attempt to divide by zero"
}

if operator in operations:
    result = operations[operator]
    print(f"result : {result}")
else:
    print("Error: Invalid operator")


#Task 3
dct = {i:i**2 for i in range(1,11)}
print(dct)


#Task 4
departments = {
    'Network Administrator': [
        {'first_name': 'george', 'last_name': 'Williams', 'age': 36, 'salary': 5000},
        {'first_name': 'nick', 'last_name': 'Jones', 'age': 22, 'salary': 6000}
    ],
    'Database Administrator': [
        {'first_name': 'michael', 'last_name': 'Anderson', 'age': 22, 'salary': 6000},
        {'first_name': 'alex', 'last_name': 'Jones', 'age': 23, 'salary': 5500}
    ],
    'Project Manager': [
        {'first_name': 'martin', 'last_name': 'Williams', 'age': 32, 'salary': 8800},
        {'first_name': 'daniel', 'last_name': 'Richards', 'age': 41, 'salary': 7500}
    ],
}
avg_salaries = {}

for department, employees in departments.items():
    total_salary = 0
    for employee in employees:
      total_salary += employee['salary']
    avg_salary = total_salary / len(employees)
    avg_salaries[department] = avg_salary

print(avg_salaries)
