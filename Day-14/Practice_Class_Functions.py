#Create a function to print "Welcome to Python".
def Greet():
    print("Welcome to Python")
Greet()

#Create a function to accept a name and print a greeting.
def User(name):
    print(f"Hello {name} Good Morning!!")
User("Ruchi")

#Create a function to add two numbers using return type and arguments.
def add(num1,num2):
    Total = num1+num2
    return Total
print("The sum of two numbers is:",add(20,30))

#Create a function to add two numbers with arguments and without return type.
def add(num1,num2):
    Total = num1 + num2
    print("The sum of two numbers is:",Total)
add(20,40)


#Create a function to subtract two numbers with args and without return type.
def sub(num1,num2):
    difference = num1-num2
    print("The difference of two numbers is:",difference)
sub(20,30)

#Create a function to subtract two numbers with args and with return type.
def sub(num1,num2):
    difference = num1 - num2
    return difference
ans = sub(40,20)
print(ans)

#Create a function to check whether a number is even or odd.
def Check_E_O(num):
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
num = int(input("Enter a number:"))
Check_E_O(num)

#Create a function to check whether a number is even or odd with return type.
def Check_E_O(num):
    if num % 2 == 0:
       return "Even"
    else:
        return "Odd"
num = int(input("Enter a number:"))
print(Check_E_O(num))

#Create a function to find the square of a number.
def Square_Number(num):
    return num ** 2
num = int(input("Enter a number:"))
r=Square_Number(num)
print("The square of a number is:",r)

#Create a function to calculate the area of a circle with args and return type.
import math
def circle(radius):
    area = (math.pi *(radius ** 2))
    return area
r=circle(4)
print(r)

#Create a function to calculate the area of a circle
import math
def area_circle(radius):
    area = math.pi *(radius **2)
    print("The area of a circle is :",area)
area_circle(4)

#Create a function to calculate the area of a rectangle.
def area_rectangle(Length,Width):
    area = Length * Width
    return area
r=area_rectangle(4,5)
print("The area of a rectangle is :",r)

#Create a function to calculate the area of a rectangle without return type.
def area_rectangle(length,width):
    area = length * width
    print(f"The area of a rectangle is {area}")
area_rectangle(4,5)

#Create a function to find the largest of two numbers with return type and ars.
def Largest_number(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
r=Largest_number(4,5)
print("The largest number among two is",r)

##Create a function to find the largest of two numbers
def Largest_number(num1,num2):
    if num1 > num2:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num2}")
Largest_number(24,67)

#Create a function to check whether a number is positive, negative, or zero.
def P_N_Z(num):
    if num > 0:
        print(f"The number {num} is Positive Number")
    elif num < 0:
        print(f"The number is {num} is Negative Number")
    else:
        print(f"The number is {num} is zero")
P_N_Z(24)

