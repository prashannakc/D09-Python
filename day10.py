#single inheritance
class Parent():
    a = 10
    b = 11

    def __init__(self, a):
        print("I am from parent. ", a)

    def add(self):
        print("this is from add method in parent class")


class Child(Parent):
    a =111
    d = 1
    def __init__(self, c):
        print("I am from child", c)
        super().__init__(1)  #Parent.__init__(self)

    def test(self):
        print("this is test method from class child")

obj = Child(23)
print(obj.a)
obj.add()
obj.test()


#CA
class Person():
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Student(Person):
    def __init__(self, name, SID):
        self.SID = SID
        super().__init__(name)

    def show_details(self):
        return self.name, self.SID

class Test(Student):
    def hello(self):
        return f"\nHello {self.name}"

obj = Student('Prashanna', 1234)  
print(obj.show_name())
for i in obj.show_details():
    print(i, end=" ")
obj2 = Test('PKC', 123)  
print(obj2.hello()) 


#CA 2 
class Person(): 
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def display_person(self): 
        return f"{self.name}\n {self.age}" 
    
class Patient(Person):
    def __init__(self, name, age, PID):
        self.PID = PID
        super().__init__(name, age)

    def display_patient(self):
        return f"{self.PID} | {self.name} | {self.age}"
    
class InPatient(Patient):
    def __init__(self, name, age, PID, RN):
        self.RN = RN
        super().__init__(name, age, PID) 

    def display_inpatient(self):
        return f"{self.PID} | {self.name} | {self.age} | {self.RN}" 
    
obj = InPatient("Prashanna", 23, "P1", "R2") 
print(obj.display_inpatient()) 

         
    


