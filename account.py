# James Bankole 11/11/16 Unit 9 Project
# This program has a class that models a banking system and then a second program testing it.


class Account:
    """This class models a banking system."""
    def __init__(self, name, accountNumber, balance = 0):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance


    def deposit(self, amount):
        """The user inputs an amount to deposit, then the amount is added to the user's balance."""
        self.balance += amount

    def withdraw(self, amount):
        """If the user is withdrawing an amount less than their balance,
         then the amount is subtracted from the balance."""
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False

    def showBalance(self):
        return (self.balance)

    def __str__(self):
        """This method displays the user's name and their balance."""
        return self.name +", your balance is: " + str(self.balance)
