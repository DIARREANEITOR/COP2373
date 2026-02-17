from functools import reduce

expenses = []

num = int(input("How many expenses do you have? "))

for i in range(num):
    expense_type = input(f"\nExpense {i+1} type: ")
    amount = float(input(f"Expense {i+1} amount: $"))
    expenses.append({"type": expense_type, "amount": amount})

total   = reduce(lambda acc, e: acc + e["amount"], expenses, 0)
highest = reduce(lambda a, b: a if a["amount"] > b["amount"] else b, expenses)
lowest  = reduce(lambda a, b: a if a["amount"] < b["amount"] else b, expenses)

print("\n Results ")
print(f"Total Expenses:   ${total:.2f}")
print(f"Highest Expense:  {highest['type']} - ${highest['amount']:.2f}")
print(f"Lowest Expense:   {lowest['type']} - ${lowest['amount']:.2f}")