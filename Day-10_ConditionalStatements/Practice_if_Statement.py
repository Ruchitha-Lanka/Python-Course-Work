#1.Write a Python program that checks if a number is positive.
number = int(input("Enter a number:"))
if number > 0:
    print(f"{number} is positive")

#2.Write a Python program that checks if a given string is empty.
string = input("Enter a string:")
if string == "":
    print(f"{string} is empty")

#3.Write a Python program that determines if a number is positive, negative, or zero using only if statements and no elif or else.
number = int(input("Enter a number:"))
if number > 0:
    print("Positive")
if number < 0:
    print("Negative")
if number == 0:
    print("Zero")

#4.Write a Python program that checks if a number is a multiple of both 3 and 5.
number = int(input("Enter a number:"))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is multiple of 3 and 5")

#6.Write a Python program that checks if a number is divisible by both 2 and 3.
number = int(input("Enter a number:"))
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3")

#7.Write a Python program that checks if a given number is a multiple of 4.
number = int(input("Enter a number:"))
if number % 4 == 0:
    print(f"{number} is multiple of 4")

#8.Write a Python program that determines if a number is a perfect cube.
number = int(input("Enter a number:"))
if round(int(number ** (1/3)**3)) == number:
    print(f"{number} is a perfect cube")

#5.Write a Python program that determines if a given number is a perfect square.
number = int(input("Enter a number:"))
if int(number ** 0.5)**2 == number:
    print(f"{number} is a perfect square")