from Account import Account


class Savings(Account):

    def __init__(self, owner,
                 balance=0,
                 withdrawal_limit=100):

        super().__init__(owner, balance)

        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):

        if amount > self.withdrawal_limit:

            print(
                f"Withdrawal amount exceeds "
                f"the limit of {self.withdrawal_limit}"
            )

        else:
            super().withdraw(amount)


print("---Savings Account---")

savings = Savings(
    "Alice",
    1000,
    100
)

print(
    f"Initial balance: "
    f"{savings.get_balance()}"
)

savings.deposit(500)

print(
    f"Current balance: "
    f"{savings.get_balance()}"
)

savings.withdraw(100)

print(
    f"Final balance: "
    f"{savings.get_balance()}"
)
