#Write a Python program that determines if a number is a perfect cube.
num = int(input("Enter a number:"))
if round(num ** (1/3)) ** 3 == num:
    print(f"{num} is a perfect cube")