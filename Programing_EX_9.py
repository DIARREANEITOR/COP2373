class BankAcct:
    def __init__(self, name, acct_num, amount, interest_rate):
        self.name = name
        self.acct_num = acct_num
        self.balance = float(amount)
        self.interest_rate = float(interest_rate)

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = float(new_rate)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def calculate_interest(self, days):
        return self.balance * self.interest_rate * (days / 365)

    def __str__(self):
        return (f"\nHolder: {self.name} | Acct: {self.acct_num}\n"
                f"Balance: ${self.balance:,.2f} | Rate: {self.interest_rate:.2%}")


def test_bank_account():
    # User inputs
    name = input("Enter account holder name: ")
    number = input("Enter account number: ")
    amount = float(input("Enter initial balance: "))
    rate = float(input("Enter interest rate (For example 0.05 for 5%): "))

    # Object creation
    acct = BankAcct(name, number, amount, rate)
    print(acct)

    # Manual operations
    dep = float(input("\nEnter amount to deposit: "))
    acct.deposit(dep)

    wit = float(input("Enter amount to withdraw: "))
    acct.withdraw(wit)

    days = int(input("Enter days to calculate interest: "))
    interest = acct.calculate_interest(days)

    print(f"Calculated Interest ({days} days): ${interest:.2f}")
    print(acct)


if __name__ == "__main__":
    test_bank_account()