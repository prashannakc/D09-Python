'''
class Test():
    a = 10              a and b = attributes of Test
    b = 11


    def testing(*args, **kwargs):
        return 1
'''
'''
class Math():
    a=11
    b=10

    def add(self):
        c = 10 #local variable
        self.c = 10 #global variable
        return self.a + self.b
    def sub(self):
        return self.add() - self.c

obj = Math()
print(obj.a)

obj1 = Math()
obj1.c = 1100
print(obj1.c)

obj2 = Math()
#print(obj2.c) error(c only on object 1)

print(obj.add()) 
print(obj1.c - obj1.sub())
print(obj.sub())
'''



class Mathh():
    def __init__(self, a, b): #constructor (a,b only exist here)
        print(a, b)
        self.a = a  #now global
        self.b = b
        print("hello, i'm here")

    def add(self):
        self.c = 10 
        return self.a + self.b
    def sub(self):
        return self.add() - self.c
    
object = Mathh(1, 2)


#CA
class BankAccount():
    def __init__(self, acc_num, name, acc_type, ini_bal):
        self.ini_bal = ini_bal
        self.acc_num = acc_num
        self.name = name
        self.acc_type = acc_type

        if self.ini_bal < 0:
            print("Initial balance cannot be negative.")
            self.ini_bal = 0

        self.status = "Inactive"
        self.set_account_status()

    def get_minimum_balance(self):
        if self.acc_type.lower() == "savings":
            return 1000
        elif self.acc_type.lower() == "current":
            return 5000
        else:
            raise ValueError("Invalid account type. Must be 'savings' or 'current'.")
    
    def check_min_balance(self):
        if self.ini_bal >= self.get_minimum_balance():
            print("Balance met")
            return True
        print("Balance below required")
        return False
    
    def set_account_status(self):
        if self.check_min_balance():
            self.status = "Active"

    def display_account_details(self):
        print("----- Account Details -----")
        print("Account Number :", self.acc_num)
        print("Holder Name    :", self.name)
        print("Account Type   :", self.acc_type)
        print("Balance        :", self.ini_bal)
        print("Account Status :", self.status)
        print("---------------------------")



account1 = BankAccount(
    acc_num = 101,
    name="Ram Sharma",
    acc_type="Savings",
    ini_bal=500
)

account1.display_account_details()


        

