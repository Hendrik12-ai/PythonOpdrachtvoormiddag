from Bankaccount import BankAccount

def test_constructor():
    account = BankAccount("123456", 1111, "Test User", 1000)
    if account.account_id != "123456":
        print(" account_id wrong")
    if account.pin_code != 1111:
        print("account pin wrong")
    if account.holder_name != "Test User":
        print(" holder_name wrong")
    if account.balance != 1000:
        print(" balance wrong")

def test_deposit():
    account = BankAccount("123456", 1111, "Test User", 1000)
    account.deposit(500)
    if account.balance != 1500:
        print(" deposit wrong")

def test_withdraw():
    account = BankAccount("123456", 1111, "Test User", 1000)
    account.withdraw(200)
    if account.balance != 800:
        print("withdraw wrong")


def test_str():
    account = BankAccount("123456", 1111, "Test User", 1000)
    expected_str = 'Account id is 123456 with pincode 1111. The cardholder is named Test User with a balance of 1000 euros.'
    if str(account) != expected_str:
        print("Fout: __str__ output wrong")

test_constructor()
test_deposit()
test_withdraw()
test_str()

print("all tests have concluded.")

