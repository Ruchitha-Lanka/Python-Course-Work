'''#1.Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.
number = int(input("Enter a number:"))
i = 1
while i <= number:
    print(i)
    i = i + 1

#2.Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.
number = int(input("Enter a number:"))
while number != 0:
    print(number)
    number = number -1

#3.Write a while loop that calculates the sum of even numbers from 1 to 100.
number = int(input("Enter a number:"))
i = 1
sum = 0
while i <= number:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)

#4.Create a simple number guessing game using a while loop. Generate a random number and have the user guess it, giving hints like "too high" or "too low" until they guess correctly.
original_number = int(input("Enter a number:"))
guess_number = int(input("Enter a guess number:"))
while original_number != guess_number::
    if original_number == guess_number:
        print("Correct guess")
    elif original_number > guess_number:
        print("Too high!")
    elif original_number < guess_number:
        print("Too Less")
    else:
        print("Invalid Number")
print("End")
#5.Use a while loop to calculate the factorial of a given number.
number = int(input("Enter a number:"))
fact = 1
i = 1
while i <= number:
    fact = fact * i
    i = i +1
print(fact)

#6.Write a while loop that prints all even numbers between 1 and 50.
number = int(input("Enter a number:"))
sum = 0
i = 1
while i <= number:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)'''

#7.Create a program that calculates the sum of the digits of a given integer using a while loop.
number = int(input("Enter a number:"))
sum = 0
while number != 0:
    r = number % 10
    sum = sum + r
    number = number // 10
print(sum)

#8.Generate a multiplication table for a given number using a while loop.
number = int(input("Enter a number:"))
i = 1
while i <= 10:
    table = i * number
    print(f"{i} x {number} = {table}")
    i = i + 1

#9.Write a program to find all the factors of a given number using a while loop.
number = int(input("Enter a number:"))
sum = 0
i=1
while i <= number:
    if  number % i == 0:
        sum = sum + i
    i = i + 1
print(sum)

#10.Implement a program that reverses even numbers using a while loop.
number = int(input("Enter a number:"))
while number != 0:
    r = number % 10
    if r % 2 == 0:
        print(r,end="")
    number = number //10

#11.Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.
correct_password = input("Enter password:")
Enter_password = input("Enter password:")
while correct_password  != Enter_password:
    print("Passwords do not match")
    Enter_password = input("Enter password:")
    if correct_password == Enter_password:
        print("Passwords do match")


