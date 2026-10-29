unit = input("ENter C or F:")
num = float(input("ENter a number:"))
if unit == "C":
    Celsius = num - 32 * 5/9
    print(f"{Celsius:.3f}")
elif unit == 'F':
    Fahrenheit = (num * 9 / 5) + 32
    print(f"{Fahrenheit:.2f}")
else:
    print("Please enter C or F")