First_num = int(input("Enter a number:"))
Second_num = int(input("Enter anumber:"))
diff = First_num - Second_num
if diff > 0:
    print(f"{diff} is apositive number")
elif diff < 0:
    print(f"{diff} is a negative number")
else:
    print(f"{diff} is zero")