
from Bankaccount import BankAccount
accounts = [ BankAccount("0174953", 1111, "Hendrik", 400000), BankAccount("123456", 2222, "Steven", 500000), BankAccount("654321", 3333, "Maarten", 300000) ]
print(accounts)
Hendrik = BankAccount("1111111",2222, "Hendrik", 100 )
Hendrik.deposit(42.00)
print(accounts)
Hendrik.withdraw(72.00)
print(Hendrik.balance)


def find_account(accounts, account_id):
    for account in accounts:
        if account.account_id == account_id:
            return account
    return None

def atm_application():
    print(f'''  
             *******************
             *******************
             *      ATM APP    *
             *******************
             *******************''')


    account_id = input("Enter your account id: ")
    account = find_account(accounts, account_id)

    if account:
        attempts = 0
        while attempts < 3:
            pin = int(input("Enter your pin: "))
            if pin == account.pin_code:
                print(f"Welcome, {account.holder_name}")
                while True:
                    print(f"Your balance is {account.balance}")
                    choice = input('''Do you want to:
                           *1) withdraw
                           *2) deposit
                           *3) exit \n''')
                    if choice.lower() == "exit" or choice.lower() == "3":
                        print("Terminating session")
                        return
                    elif choice.lower() == "2" or choice.lower() == "deposit":
                        amount = float(input("How much do you want to deposit? "))
                        account.deposit(amount)
                        print(f"New balance: {account.balance}")
                    elif choice.lower() == "1" or choice.lower() == "withdraw":
                        amount = float(input("How much do you want to withdraw? "))
                        account.withdraw(amount)
                        print(f"New balance: {account.balance}")
                    else:
                        print("wrong input, please try again.")
            else:
                attempts += 1
                print("Wrong pin")
        print("Too many failed attempts. Terminating session.")
    else:
        print("Wrong account id")

atm_application()
