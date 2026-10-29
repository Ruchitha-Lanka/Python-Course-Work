#Write a Python program that determines if a given number is a perfect square.
num = int(input("Enter a number:"))
if int(num ** 0.5) ** 2== num:
    print(f"{num} is a perfect sqaure")