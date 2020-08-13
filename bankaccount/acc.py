class Account:

    def __init__(self,path):
        self.path = path
        with open(path,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

        with open(self.path,'w') as file:
            file.write(str(self.balance))

    def deposit(self,amount):
        self.balance = self.balance + amount

        with open(self.path,'w') as file:
            file.write(str(self.balance))

account = Account("bankaccount/balance.txt")

print(account.balance)

account.withdraw(200)
print(account.balance)

account.deposit(100)
print(account.balance)