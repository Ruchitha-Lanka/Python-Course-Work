#Write a Python program that checks if a given year is a century year (ending in '00').
year = int(input("Enter a number:"))
if year % 100 == 00:
    print(f"{year} is a century year")
else:
    print(f"{year} is not a century year")