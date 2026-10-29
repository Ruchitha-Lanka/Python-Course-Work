#Print a simple pattern of increasing asterisks.
for i in range(1,5):
    for j in range(i):
        print("*",end = " ")
    print()

#Print a simple pattern of decreasing asterisks
for i in range(5,-1,-1):
    for j in range(i):
        print("*",end= " ")
    print()

#Print a pattern of right-aligned asterisks with spaces.
r=5
for i in range(1,5):
    for k in range(r-i):
        print(" ",end = " ")
    for j in range(i):
        print("*", end = " ")
    print()

#Print a pattern of left-aligned asterisks with spaces.
for i in range(1,5):
    for j in range(i):
        print("*",end = " ")
    print()

#Print a pyramid pattern with spaces.
r=5
for i in range(1,6):
    for k in range(r-i):
        print(" ",end = "")
    for j in range(i):
        print("*",end = " ")
    print()

#Print an inverted pyramid pattern with spaces.
r=6
for i in range(6,-1,-1):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end = " ")
    print()

#Print a hollow square pattern.
n = int(input("ENter a number:"))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#print diagonal of a square matrix
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        if i == j or i +j == (n-1):
            print("*",end = " ")
        else:
            print(" ",end= " ")
    print()

#Print a diamond pattern.
r=6
n = int(input("Enter a number:"))
for i in range(1,n+1):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
r=6
for i in range(5,0,-1):
    for k in range(r-i):
        print(" ",end = "")
    for j in range(i):
        print("*",end = " ")
    print()

#Print a hollow half pyramid pattern
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        if j == 0 or i == j or i == n-1:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

#Print an hourglass pattern
r=6
for i in range(6,0,-1):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
r=6
for i in range(2,7):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

#Print a checkered pattern of stars and spaces
for i in range(1,6):
    for j in range(1,6):
        if i % 2 == 0:
            print(" *",end="")
        else:
            print("*",end=" ")
    print()
#Hollow Triangle


