#Write a Python program that calculates the final price of an item after applying a discount based on the purchase amount.
purchase = int(input("Enter a number:"))
discount = int(input("Enter discount:"))
if purchase >= 1000:
    pay = int(purchase * discount)/100
    final = purchase - pay
    print(final)
else:
    print(purchase)


