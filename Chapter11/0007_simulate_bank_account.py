"""
Program 11.5
Simulate a Bank Account with Support for
depositMoney, withdrawMoney, showBalance operations
"""


class BankAccount:
    def __init__(self, name):
        self.user_name = name
        self.balance = 0.0

    def show_balance(self):
        print(f"{self.user_name} has a balance of {self.balance} dollars")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("You don't have sufficient funds in your account")
        else:
            self.balance -= amount
            print(f"{self.user_name} has withdrawn {amount} dollars")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"{self.user_name} has deposited {amount} dollars")


def main():
    savings_account = BankAccount("Olivia")
    savings_account.deposit_money(1000)
    savings_account.show_balance()
    savings_account.withdraw_money(500)
    savings_account.show_balance()
    savings_account.withdraw_money(1000)
    savings_account.show_balance()


if __name__ == "__main__":
    main()
