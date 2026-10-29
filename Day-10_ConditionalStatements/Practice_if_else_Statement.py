'''#1.Write a Python program that checks if a given year is a leap year.
year = int(input("Enter a year:"))
if year % 4 == 0 or (year % 400 == 0 and year % 100 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a leap year")

#2.Write a Python program that checks if a given character is a vowel or a consonant.
ch = input("Enter a character:")
if ch in "aeiouAEIOU":
    print(f"{ch} is a vowel")
else:
    print(f"{ch} is consonant")

#3.Write a Python program that checks if a given year is a century year (ending in '00').
number = int(input("Enter a number:"))
if number % 100 == 00:
    print(f"{number} is ending with century year")
else:
    print(f"{number} is not ending with the century year")

#4.Write a Python program that checks if a given number is prime.
number = int(input("Enter a number:"))
count = 0
for i in range(1,number + 1,1):
    if number % i == 0:
        count = count +1
if count == 2:
    print(f"{number} is a prime number")
else:
    print("Not a prime number")

#5.Write a Python program that checks if a number is positive or non-positive (including zero).
number = int(input("Enter a number:"))
if number > 0:
     print(f"{number} is positive")
else:
    print(f"{number} is negative")

#6.Write a Python program that compares two numbers and prints the larger one.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

#7.Write a Python program that checks if a person is eligible to vote based on their age.
age = int(input("Enter a number:"))
if age > 18:
    print(f"This persons age is {age} so eligible to vote")
else:
    print("Not eligible to vote")

#8.Write a Python program that checks if a given character is a letter or not.
ch = input("Enter a character")
if ch.isalpha():
    print("It is a Letter")
else:
    print("It is not a Letter")

#9.Write a Python program that finds and prints the smallest of three numbers without using inbuilt methods.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
if num1 < num2 and num1 < num3:
    print(f"{num1} is smallest ")
elif num2 < num3:
    print(f"{num2} is smallest")
else:
    print(f"{num3} is smallest")

#10.Write a Python program that finds and prints the largest of four numbers.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
num4 = int(input("Enter a number:"))
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is largest number")
elif num2 > num3 and num2 > num4:
    print(f"{num2} is largest number")
elif num3 > num4:
    print(f"{num3} is largest number")
else:
    print(f"{num4} is largest number")'''

#11.Write a Python program that takes two numbers as input and determines the sign of their difference.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
sign = input("Enter a sign:")
if sign == "+":
    output = num1 + num2
    print(output)
elif sign =="-":
    output = num1 - num2
    print(output)
elif sign == "*":
    output = (num1 )*( num2)
    print(output)
elif sign == "/":
    output = num1 / num2
    print(output)
else:
    print("Not a number")

#12.Write a Python program that checks if a number is a multiple of 7 or not.
num = int(input("Enter a number:"))
if num % 7 == 0:
    print(f"{num} is a multiple of 7")
else:
    print(f"{num} is not a multiple of 7")

#13.Write a Python program that calculates and prints the absolute value of a given number.
number = int(input("Enter a number:"))
if number > 0:
    print(number)
else:
    print(abs(number))