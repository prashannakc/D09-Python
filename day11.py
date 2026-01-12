#multiple inheritance 
class A(): 
    __a = 100 #private (inaccessible) only class can use it not even object
    __api_key = "12m,2123123123"
    b=0

    def __data(self):   #private method
        return self.__api_key
    
    def data2(self):
        return self.__data()

class B(A):
    c = 100


obj = A()
print(obj.data2())


#CA
class Hospital(): 
    __hospital_name = "Norvic"
    __patients_count = 0

    def admit_patient(self, n=1):
        self.__patients_count += n
    
    def discharge_patient(self):
        if self.__patients_count <= 0:
            print("Patients count is zero")
        else:
            self.__patients_count -= 1 
    
    def get_hospital_info(self):
        return f"Hospital: {self.__hospital_name} | Patient Count: {self.__patients_count}"

class SpecialityHospital(Hospital):
    def bulk_admit(self, n):
        self.admit_patient(n) 
    

obj = SpecialityHospital()
for i in range(10):
    obj.discharge_patient()
for i in range(1, 5):
    obj.admit_patient()
obj.discharge_patient()
obj.bulk_admit(10)
print(obj.get_hospital_info()) 

#CA 2
class BankAccount():
    __account_num = "0134143643"
    __balance = 0.00
    public_account = __account_num

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount 

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    __interest_rate = 5.2

    def add_interest(self):
        data = (self.__interest_rate/100)*self.get_balance()
        self.deposit(data) 

    def get_account_info(self):
        return f"Account Number: {self.public_account} | Balance: {self.get_balance()} | Interest Rate: {self.__interest_rate}" 
    
account = SavingsAccount()
account.deposit(5000) 
account.deposit(5000) 
account.deposit(5000) 
account.deposit(5000) 
account.withdraw(10000)
print(account.get_balance())
account.add_interest()
print(account.get_balance())
print(account.get_account_info())