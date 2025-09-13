class bankaccount:
    def __init__(self,accountholder,balance,accounttype):
        self.accountholder=accountholder
        self.balance=float(balance)
        self.accounttype=accounttype

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance is",self.balance)

    def withdraw(self,amount):

        self.balance=self.balance-amount
        
        if(self.balance<0):
            print("Insufficient funds")
        else:
            print("Balance amount", self.balance)
        
         
    def displaybalance(self):
        print("Account Holder Name",self.accountholder)
        print("Account Type",self.accounttype)
        print("Current balance",self.balance)

if __name__ == "__main__":
    bankaccount1=bankaccount("holder1",200,"savings")
    bankaccount2=bankaccount("holder1",400,"savings")

    bankaccount1.deposit(500)
    bankaccount1.displaybalance()

    bankaccount2.withdraw(300)
    bankaccount2.displaybalance()

    
    
