"""Practice exercise: process transaction records."""

transactions = [
    200,
    -50,
    500,
    -100,
    -20,
    1000
]
deposits = []
withdrawals = []

for transaction in transactions:
    if transaction > 0:
        deposits.append(transaction)
    else:
        withdrawals.append(transaction)

total_deposited = sum(deposits)
total_withdrawn = sum(withdrawals)
balance = total_deposited + total_withdrawn

print(f"Total deposited: {total_deposited}")
print(f"Total withdrawn: {abs(total_withdrawn)}")
print(f"Balance: {balance}")


    
