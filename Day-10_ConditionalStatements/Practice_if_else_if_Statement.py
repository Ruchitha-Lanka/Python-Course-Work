#1.Write a Python program that converts letter grades (A, B, C, D, F) to their equivalent GPA values.
marks = int(input("Enter a number:"))
if marks  > 90:
    print(f"For {marks} A grade")
elif 80 <= marks <= 90:
    print(f"For {marks} B grade")
elif 70 <= marks <= 60:
    print(f"For {marks} C grade")
elif 50 <= marks <= 40:
    print(f"For {marks} D grade")
elif marks < 40:
    print(f"{marks} F grade")
else:
    print("Absent")

