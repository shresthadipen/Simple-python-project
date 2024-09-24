class Account:
    def __init__(self):
        self.balance = 0
        self.amount = 0
        self.debit = 0

    def setName(self, name):
        self.name = name

    def setAmount(self, amount):
        self.amount += amount  

    def setAccountNumber(self, accountNumber):
        self.accountNumber = accountNumber
        
    def setDebit(self, debit):
        self.debit = debit
            

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def getAccountNumber(self):
        return self.accountNumber

    def getBalance(self):
        total_balance = self.balance + self.amount
        return total_balance
    
    def withdraw(self):
        if self.amount <  self.debit:
            return False
        else:
            self.amount -= self.debit
            return self.amount

    def greet(self):
        print(f"Welcome {self.name}!!!")

account = None
choice = ''
while(choice != '5'):
    print("***** Choose Options *****\n1. New Account\n2. Deposit amount\n3. Check Balance\n4. Withdraw\n5. Exit")
    choice = input("Enter your choice from (1-5): ")

    if choice == '1':
        account = Account() 
        name = input("Enter your name: ")
        accountNumber = int(input("Enter account number: "))
        amount = int(input("Enter an initial balance you want to add: "))
    
        account.setName(name)
        account.setAccountNumber(accountNumber)
        account.setAmount(amount)

    elif choice == '2':
        if account:
            account.greet()
            deposit_amount = int(input("Enter an amount you want to deposit: Rs. "))
            account.setAmount(deposit_amount)
            print("Amount deposited successfully.")
        else:
            print("Account not created!!! Choose option 1 first")

    elif choice == '3':
        if account:
            account.greet()
            print(f"Your current balance is Rs. {account.getBalance()}")
        else:
            print("Account not created!!! Choose option 1 first")

    elif choice == '4':
        if account:
            account.greet()
            debit = int(input("Enter an amount you want to withdraw: Rs. "))
            account.setDebit(debit)
            remaining_balance = account.withdraw()
            if remaining_balance == False: 
                print(f"You have not enough balance")
            else:
                print(f"You have withdrawn Rs. {debit}")
                print(f"Your Total amount is Rs. {remaining_balance}")
                
        else:
            print("Account not created!!! Choose option 1 first")
            
    elif(choice == '5'):
        if account:
            print(f"Thank you {account.name}!! for  using this system")
            
        else:
            print("Exit")
        
    else:
        print("Invalid Option")