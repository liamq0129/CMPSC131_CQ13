class SavingsAccount:
    def __init__(self, account_id, balance, previous_balance, annual_interest_rate):
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate
    def set_interest_rate(self, updated_interest_rate):
        self.annual_interest_rate = updated_interest_rate
    def get_monthly_interest_rate(self):
        return self.annual_interest_rate/100/12
    def get_monthly_interest(self):
        return self.get_monthly_interest_rate()*self.balance
    def get_balance_change_percent(self):
        return ((self.balance-self.previous_balance)/self.previous_balance) * 100
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
    def deposit(self,amount):
        self.balance += amount

      
def cq():
    account = SavingsAccount(1122,20_000.0,18_500.0, 4.5)

    account.withdraw(2500.0)
    account.deposit(3000.0)

    print(f"Account id: {account.account_id}\nCurrent Balance: {account.balance}\nMonthly Interest Rate: {account.get_monthly_interest_rate()*100}%\nMonthly Interest: {account.get_monthly_interest():.2f}\nPercentage Change: {account.get_balance_change_percent():.2f}%")


if __name__ == "__main__":
    cq()
