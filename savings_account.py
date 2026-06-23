from Account import Account


class Savings(Account):

    def __init__(self, owner, balance=0, withdrawal_limit=100):
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


savings = Savings("Alice", 1000, 100)

savings.withdraw(50)
savings.withdraw(150)
