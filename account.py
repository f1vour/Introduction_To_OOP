class Account:

    def __init__(self):
        self.balance = 10000
        self.__interest_rate = 5
        self.__id_number = "DG5785"
        print('Starting balance is: ', self.balance)

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number

    def get_interest_rate(self):
        return self.__interest_rate

    def deposit(self, amount):
        self.balance = amount + self.balance
        print('New balance is: ', self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount


account = Account()
account.deposit(1000)
