#Write a Python program that calculates the final price of an item after applying a discount coupon code.
price = int(input())
#discount = int(input())
Coupon = input()
if Coupon == "Save10":
    discount = price * 10 /100
    price = price - discount
    print(discount,price)
elif Coupon == "Save20":
    discount = price * 20 /100
    price = price - discount
    print(discount,price)
else:
    print("Invalid Coupon")