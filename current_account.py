from account import Account


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)


currentAccount = CurrentAccount()
currentAccount.deposit(5000)
currentAccount.withdraw(1500)
