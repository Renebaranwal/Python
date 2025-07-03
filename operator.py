balance = 5000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    print("Please collect your cash.")
    balance -= withdraw
    print("Remaining balance:", balance)
else:
    print("Insufficient balance.")
