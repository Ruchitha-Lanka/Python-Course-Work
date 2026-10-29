#Write a Python program that simulates an ATM machine, allowing users to check their balance and withdraw money.
total_money = int(input("Enter total money:"))
check = input("Enter check balance or withdraw or deposit:")
if check == "check_balance":
    print("total_money")
elif check == "withdraw":
    withdraw_money = int(input("Enter amount:"))
    withdraw = total_money - withdraw_money
    total_money = total_money - withdraw_money
    if withdraw > total_money:
        print("Not sufficient balance")
    else:
        print(withdraw)
elif check == 'deposit':
    deposit_money=int(input("Enter amount:"))
    deposit = total_money + deposit_money
    total_money = total_money+deposit_money
    print(deposit)
else:
    print("Invalid")
print(total_money)


