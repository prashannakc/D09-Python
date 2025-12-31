#multiple keyword data(arbitary keyword argument)
def data(**kwargs):
    print(kwargs)

data(a = 10, b = "test", c =11)

def fields(**info):
    if "name" in info and "email" in info and "phone" in info:
        print(f"name: {info['name']}\nemail: {info['email']}\nphone: {info['phone']}")
    else:
        print("Keys not found")

fields(name = "Prashanna", email = "abcdefg@gmail.com", phone = 9000)

import datetime


def error_catching(**kwargs):
    if len(kwargs)==0:
        return "please provide kwargs"
    elif 'message' not in kwargs.keys():
        return "message key is compulsory"
    return f"{kwargs.get('level') if 'level' in kwargs.keys() else ''} {kwargs.get('message')} {kwargs.get('time_stamp') if 'time_stamp' in kwargs.keys() else ''}"


time = datetime.datetime.now().strftime("%H:%M:%S")
print(error_catching(message = "this is testing", level = "WARNING", time_stamp = time))
print(error_catching(message = "this is testing", level = "WARNING"))
print(error_catching(message = "this is testing"))


def student_info(*marks, **info):
    sum = 0
    for i in marks:
        sum += i
    avg = sum/len(marks)
    name = info.get('name')
    return f"Average marks of {name} is {avg}.\n"

print(student_info(40, 50, 70, name="prashanna", address="kathmandu"))

#RECURSION
def fibo(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fibo(n-1)
    
print(fibo(5))
