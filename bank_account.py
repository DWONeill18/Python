# Bank Account
# A class that can be used to create and manipulate a personal bank account.

class BankAccount(object):
    balance = 0
    # When creating an object of the class, the name will be attributed to that class.
    def __init__(self, name):
        self.name = name

    #Defines what represents the object when a user tries to print that object.
    def __repr__(self):
        return "Account name: %s, Balance: $%.2f" % (self.name, self.balance)

    # Method for showing the bank balance
    def show_balance(self):
        print("Balance: $%.2f" % (self.balance))

    # Method allowing deposits into the account
    def deposit(self, amount):
        if amount <= 0:
            print("Amount not valid, needs to be positive value.")
            return
        else:
            print("Depositing $%.2f" % (amount))
            self.balance += amount
            self.show_balance()

    # Method to allow withdrawals
    def withdraw(self, amount):
        if amount > self.balance:
            print("Amount exceeds current balance.")
            return
        else:
            print("Withdrawing $%.2f" % (amount))
            self.balance -= amount
            self.show_balance()

# Add an instance of the class to check its functionality
my_account = BankAccount("David")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)




