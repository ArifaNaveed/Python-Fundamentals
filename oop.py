#################    OOP IN PYTHON     ##################

class Student:
   def __init__(self, name, marks):
       self.name = name
       self.marks = marks
    
   def average(self):
       average = 0

       for lists in self.marks:
           average += lists

       average = average/3
       return average

name = "Sana"
marks = [23,45,34]
s1 = Student(name, marks)

print(s1.average())

####################################################################

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def get_debit(self, amount):
        self.balance = self.balance - amount
        print(self.account_no, "Account has been debitted by : ", amount)
        print("Balance : ", self.balance)


    def get_credit(self, amount):
        self.balance += amount
        print(self.account_no, "Account has been creditted by : ", amount)
        print("Balance : ", self.balance)



account = "79ikh"
balance = 6700
b1 = BankAccount(account, balance)
b1.get_credit(6000)
b1.get_debit(780)


