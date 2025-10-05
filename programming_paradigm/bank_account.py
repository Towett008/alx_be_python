class BankAccount:
    def __init__(self,initial_balance=0.0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance +=amount
        else:
            print("Deposit amount must be positive. ")
    def withdraw(self, amount):
        if amount <=0:
            print("Withdraw amount must be positive.")
            return False
        elif amount > self.account_balance:
            print("Insufficient funds.Withdrawal failed")
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")
      