
'''#Print a pattern of numbers in a right-angled triangle.
for i in range(1,6):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num + 1
    print()

#Print a pattern of numbers in an inverted right-angled triangle.
for i in range(6,-1,-1):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num +1
    print()

#Print a pattern of numbers with alternating rows
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
'''
#Print a pattern of numbers in an inverted pyramid.
r=6
for i in range(6,-1,-1):
    for k in range(r-i):
        print(" ",end = "")
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num +1
    print()
#Print a pattern of numbers in an inverted pyramid
r=5
for i in range(5,0,-1):
    for k in range(r-i):
        print(" ",end=" ")
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num+1
    print()
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    num = n
    for j in range(i):
        print(num,end=" ")
        num = num - 1
    print()
'''
#Print a pattern of numbers in a right-angled triangle with descending order.
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end = " ")
        num = num +1
    print()

'''