from account import Account


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("You cannot withdraw above your limit")


savingsAccount = SavingsAccount()
savingsAccount.withdraw(2000)


# method of polymorphism include the following inheritance)
# overriding(writing a method over another method:that method now has numerous forms)
# method overloading(a class having numerous methods but diff parameters)
# benefit of encapsulation is read and write

