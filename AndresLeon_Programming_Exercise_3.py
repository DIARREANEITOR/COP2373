from functools import reduce
#fix def?
#where def go
#put
def get_expenses(count):
    expenses_list = []
    for i in range(count):
        expense_type = input(f"\nExpense {i + 1} type: ")
        amount = float(input(f"Expense {i + 1} amount: $"))
        expenses_list.append({"type": expense_type, "amount": amount})
    return expenses_list

#put def
def calculate_total(expenses):
    return reduce(lambda acc, e: acc + e["amount"], expenses, 0)

#put def
def get_extreme_expense(expenses, find_max=True):
    if find_max:
        return reduce(lambda a, b: a if a["amount"] > b["amount"] else b, expenses)
    return reduce(lambda a, b: a if a["amount"] < b["amount"] else b, expenses)


#  Execution
num = int(input("How many expenses do you have? "))
if num > 0:
    data = get_expenses(num)

    total = calculate_total(data)
    highest = get_extreme_expense(data, find_max=True)
    lowest = get_extreme_expense(data, find_max=False)

    print("\n Results ")
    print(f"Total Expenses:   ${total:.2f}")
    print(f"Highest Expense:  {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest Expense:   {lowest['type']} - ${lowest['amount']:.2f}")
else:
    print("No expenses to record.")
