class BankAccount:
    def __init__(self, first_name,last_name,account_id,account_type,pin,balance): #initalisere et objekt av klassen BankAccount
        #verdier settes til instansvariabelen self., slik er de spesifikke for hvert objekt
        self.first_name=first_name
        self.last_name=last_name
        self.account_id=account_id
        self.account_type=account_type
        self.pin=pin
        self.balance=balance

    #Tre metoder
    #1) sette penger inn i banken og returnere den nye totalen
    def deposit(self,amount):
        self.balance+=amount #må kalle på instansen av balance, altså self.balance
        return self.balance
    
    def withdraw(self, amount):
        self.balance-=amount
        return self.balance #returnere den nye verdien, ettersom vi skal bruke den videre i koden
    #hvis vi kun hadde printet den hadde vi ikke oppdatert den gamle verdien. 
    
    def display_balance(self):
        return self.balance
    
    #lager et nytt bank objekt
account=BankAccount('Per', 'Ene', 12345, 'Checking', 123, 100.0)

#demonstrere da metodekall
print(account.deposit(96))
print(account.display_balance())
print(account.withdraw(25))
print(account.display_balance())

