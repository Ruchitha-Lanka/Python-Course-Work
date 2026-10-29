#Write a Python program that greets the user differently based on the time of day.
time = int(input("Enter time"))
if time < 12:
    print("Good Morning")
elif 12 <= time <= 15:
    print("Good afternoon")
elif 16 <= time <= 18:
    print("Good Evening")
elif 19 <= time <= 24:
    print("Good Night")
else:
    print("invalid time")