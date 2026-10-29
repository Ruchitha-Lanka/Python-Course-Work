#Inverted Right Angled star
for i in range(3,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#Inverted Right Angled Triangle (Left spaces)
r = 3
for i in range(3,0,-1):
    for k in range(r-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#triangle with base 6 stars
r= 6
for i in range(1,7):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()

# all equal number of Stars
for i in range(1,6):
    for j in range(1,6):
        print("*",end = " ")
    print()

# 1 1 1
# 2 2 2
# 3 3 3
for i in range(1,4):
    for j in range(1,4):
        print(i,end = " ")
    print()

# 1 2 3
# 4 5 6
# 7 8 9
num = 1
for i in range(1,4):
    for j in range(1,4):
        print(num,end = " ")
        num += 1
    print()

# A A A
# B B B
# C C C
p = 65
for i in range(1,4):
    for j in range(1,4):
        print(chr(p),end = " ")
    p = p + 1
    print()

# A B C
# A B C
# A B C
for i in range(1,4):
    p = 65
    for j in range(1,4):
        print(chr(p),end = " ")
        p = p + 1
    print()

#A B C
#D E F
#G H I
p = 65
for i in range(1,4):
    for j in range(1,4):
        print(chr(p),end = " ")
        p = p + 1
    print()
