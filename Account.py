class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print(
                f"Withdrawal successful. "
                f"Balance: {self.__balance}"
            )
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
