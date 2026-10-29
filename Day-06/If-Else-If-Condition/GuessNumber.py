#Write a Python program for a simple "Guess the Number" game. Generate a random number, and let the user guess it.
Correct_number = int(input("ENter a number:"))
Guess_number = int(input("Enter a number"))
if Correct_number == Guess_number:
    print("Correct guess!")
elif Correct_number < Guess_number :
    print("Too high!")
else:
    print("Too low!")