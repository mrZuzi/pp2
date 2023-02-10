class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
    def withdraw(self,finance):
        if(finance>self.balance):
            print("Ouuups,smth goes wrong")
        else:
            self.balance-=finance
a=Account("Khamza",1000)
b=Account("Khamza",2000)