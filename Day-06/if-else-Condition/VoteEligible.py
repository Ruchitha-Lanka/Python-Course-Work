#Write a Python program that checks if a person is eligible to vote based on their age.
Age = int(input("Enter a age:"))
if Age >= 18:
    print(f"{Age} is eligible to vote")
else:
    print(f"{Age} is not eligible to vote")