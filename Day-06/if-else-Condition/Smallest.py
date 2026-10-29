#Write a Python program that finds and prints the smallest of three numbers without using inbuilt methods.
num = int(input("Enter a number:"))
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
if num < num1 and num < num2:
    print(f"{num} is smallest number")
elif num1 < num2:
    print(f"{num1} is smallest number")
else:
    print(f"{num2} is smallest number")