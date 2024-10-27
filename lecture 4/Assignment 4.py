# Task 1
txt = str(input("Enter text: "))
normalized_txt = txt.lower()
normalized_txt = normalized_txt.replace(" ", "")
is_palindrome = normalized_txt == normalized_txt[::-1]

if is_palindrome:
    print("The text you entered is a palindrome.")
else:
    print("The text you entered is not a palindrome.")

#Task 2
text = input("Enter text: ")
ascii_values = ""

for letter in text:
    ascii_values += str(ord(letter)) + " "

print("ASCII values: {}".format(ascii_values.strip()))