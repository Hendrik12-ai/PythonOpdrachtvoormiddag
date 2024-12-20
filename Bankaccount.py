class BankAccount:
    def __init__(self, account_id, pin_code, holder_name, balance ):
        self.account_id = account_id
        self.pin_code = pin_code
        self.holder_name = holder_name
        self.balance = balance

    def deposit (self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw (self, amount):
        if self.balance < amount:
            print("not enough balance")
        else:
            self.balance = self.balance - amount
            if self.balance < 0:
                print("Can't go below zero")
            else:
                return self.balance
    def __str__(self):
        return f"Account id is{self.account_id} with pincode {self.pin_code}. The cardholder is named {self.holder_name} with a balance of {self.balance} euros."
