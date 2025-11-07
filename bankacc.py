class Bank:
    def getData(self,accno,name,acctype,balance):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=balance
    def displayUser(self):
        print("Account Number:",self.accno)
        print("Name:",self.name)
        print("Type of Account:",self.acctype)
        print("Account Balance:",self.balance)
    def displayDeposit(self):
        amt=int(input("Enter Deposit Amount:"))
        # self.amt=amt
        self.balance=self.balance + amt
        print("Available Balance: ",self.balance)
    def displayWithdraw(self):
        amt=int(input("Enter Withdraw Amount:"))
        # self.amt=amt
        if amt>self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amt
            print("Available Balance:",self.balance)
        
accno=int(input("Enter the Account Number:"))
name=input("Enter your Name:")
acctype=input("Enter the type of your Account:")
balance=int(input("Enter your Balance:"))

acc1=Bank()
acc1.getData(accno,name,acctype,balance)

while 1:
    print("\n1.Display Details \n2.Deposit \n3.Withdraw \n4.Exit \n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        acc1.displayUser()
    elif choice==2:
        acc1.displayDeposit()
    elif choice==3:
        acc1.displayWithdraw()
    elif choice==4:
        break;
    else:
        print("Invalid Choice")
        
