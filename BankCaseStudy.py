from datetime import date

class Bank:
    def __init__(self, name, accountNumber, balance, dateOfBirth, mobileNumber, emailId):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        self.dateOfBirth = dateOfBirth
        self.mobileNumber = mobileNumber
        self.emailId = emailId
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, acc):
        self.accountNumber = acc

    def getBalance(self):
        return self.balance
    
    def setBalance(self, bal):
        self.balance = bal
    
    def getDateOfBirth(self):
        return self.dateOfBirth
    
    def setDateOfBirth(self, dob):
        self.dateOfBirth = dob

    def getMobileNumber(self):
        return self.mobileNumber
    
    def setMobileNumber(self, mob):
        self.mobileNumber = mob

    def getEmailId(self):
        return self.emailId
    
    def setEmailId(self, eid):
        self.emailId = eid

    def __str__(self) -> str:
        return f"""Account Number : {self.accountNumber}  |  Name : {self.name}  |  Balance : {self.balance}  |  DOB : {self.dateOfBirth}  |  Mobile : {self.mobileNumber}  |  Email ID : {self.emailId}\n"""
    


class Transactions:
    def __init__(self, accountNumber, person, amount, dateOfTransaction, balance, message):
        self.accountNumber = accountNumber
        self.person = person
        self.amount = amount
        self.dateOfTransaction = dateOfTransaction
        self.balance = balance
        self.message = message

    def getMessage(self):
        return self.getMessage()
    def setMessage(self, message):
        self.message = message
    def getAccountNumber(self):
        return self.accountNumber

    def getPerson(self):
        return self.person
    def getAmount(self):
        return self.amount
    def getDateOfTransaction(self):
        return self.dateOfTransaction
    def getBalance(self):
        return self.balance
    def setAccountNumber(self, acc):
        self.accountNumber = acc
    def setPerson(self, person):
        self.person = person
    def setAmount(self, amount):
        self.amount = amount
    def setDateOfTransaction(self, date):
        self.dateOfTransaction = date
    def setBalance(self, balance):
        self.balance = balance
    def __str__(self) -> str:
        return f"""Account Number : {self.accountNumber}  |   Name : {self.person}  |  Amount : {self.amount}  |  Date Of Transaction : {self.dateOfTransaction}  |  Balance : {self.balance}  |  {self.message}\n"""


objectList = []
transferList = []
def check(accountNumber):
    for i in objectList:
        if i.accountNumber == accountNumber:
            return i
    return False

def createAccount(name, accountNumber, dateOfBirth, mobileNumber, emailId):
    balance = 0
    bank = Bank(name, accountNumber, balance, dateOfBirth, mobileNumber, emailId)
    objectList.append(bank)

def viewAccountDetails(accountNumber):
    if check(accountNumber):
        print(check(accountNumber).__str__())

def withdraw(accountNumber,amount):
    temp = check(accountNumber)
    if temp:
        temp.setBalance(temp.getBalance() - amount) if temp.getBalance() >= amount else print("Insufficient Balance")
    else:
        print("Account Not Found")

def deposit(accountNumber,amount):
    temp = check(accountNumber)
    temp.setBalance(temp.getBalance()+amount) if temp else print("Account  Not Found")

def transferAmount(senderAccount, receiverAccount, amount):
    senderTemp = check(senderAccount)
    receiverTemp = check(receiverAccount)
    if senderTemp and receiverTemp:
        if senderTemp.getBalance() >= amount:
            senderTemp.setBalance(senderTemp.getBalance() - amount)
            receiverTemp.setBalance(receiverTemp.getBalance() + amount)
            receiver = Transactions(person=receiverTemp.getName(),accountNumber=receiverAccount,amount = amount, dateOfTransaction=date.today(), balance = receiverTemp.getBalance(), message="Credited")
            transferList.append(receiver)
            sender = Transactions(person=senderTemp.getName(),accountNumber=senderAccount,amount = amount, dateOfTransaction=date.today(), balance = senderTemp.getBalance(), message="Debited")
            transferList.append(sender)
        else:
            print("Insufficient balance")
    else:
        print("Sender / Receiver Accounts Not Found")
def printTransactions(accountNumber):
    temp =  check(accountNumber)
    flag = 0
    if temp:
        for i in transferList:
            if i.getAccountNumber() == accountNumber:
                print(i.__str__())
                flag = 1
        if flag == 0:
            print("No transactions done")
    else:
        print("Account Not found")



# import Bank
# import Transfer
# import Controller

# controller = Controller()
while True:
    print("\n 1.Create Account \n 2.Deposit \n 3.Withdraw \n 4.Fund Transfer \n 5. Transaction Details  \n 6.View Account details by accno \n 7. Exit \n ")
    c = int(input("Enter the service you need : "))
    if c==1:
        name = input("Enter Name : ")
        accountNumber = int(input("Enter Account Number : "))
        dateOfBirth = input("Enter DOB (DD/MM/YYYY) format : ")
        mobileNumber = input("Enter Mobile Number : ")
        emailId = input("Email ID : ")
        createAccount(name, accountNumber, dateOfBirth, mobileNumber, emailId)
        continue
    elif(c==2):
        accountNumber = int(input("Enter Account Number : "))
        amount = int(input("Enter Amount : "))
        deposit(accountNumber,amount)
        continue
    elif(c==3):
        accountNumber = int(input("Enter Account Number : "))
        amount = int(input("Enter Amount : "))
        withdraw(accountNumber,amount)
        continue
    elif(c==4):
        senderAccount = int(input("Enter Sender Account Number : "))
        receiverAccount = int(input("Enter Receiver Account Number : "))
        amount = int(input("Enter Amount to be transferred : "))
        transferAmount(senderAccount, receiverAccount, amount)
        continue
    elif(c==5):
        accountNumber = int(input("Enter Account Number : "))
        printTransactions(accountNumber)
        continue
    elif(c==6):
        accountNumber = int(input("Enter Account Number : "))
        viewAccountDetails(accountNumber)
        continue
    elif(c==7):
        break
    else:
        print("Enter correct Option")
