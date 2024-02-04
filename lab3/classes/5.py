class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful, new balance: ${self.balance}")
        else:
            print("error")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful, new balance: ${self.balance}")
            else:
                print("Withdrawal canceled")
        else:
            print("error")

account = BankAccount(owner="John Doe", initial_balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(-100)
account.withdraw(-50) 

print(f"Final balance for {account.owner}: ${account.balance}")