# Task 1
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

result = num1 + num2 + num3
print(result)

# Task 2
side_length = int(input("Please enter the side length of the cube: "))
volume = side_length ** 3
surface_area = 6 * (side_length ** 2)

print(volume)
print(surface_area)

# Task 3
price_monitor = float(input("Please enter the price of monitor: "))
price_system_block = float(input("Please enter the price of system block: "))
price_keyboard = float(input("Please enter the price of keyboard: "))
price_mouse = float(input("Please enter the price of mouse: "))

total_price = (price_monitor + price_system_block + price_keyboard + price_mouse)
print(total_price)