'''
data={
    'name':'ram',
    'class': 13,
    'status': True
}

for i in data:
    print(data)

for i in data.values():
    print(i)

for i in range(1,101,4):
    print(i)

string_list = [
    "python_programming",
    "learn_data_science",
    "backend_development"
]

b = len(string_list)
print(b)
for i in range(0, b):
    print(string_list[i])

for i in range(1,10):
    if i==5:
        print("five")
        break

for i in range(1,10):
    if i==5:
        print("five")
        continue
    print(i)

for i in [1,2,3,4]:
    for j in [5,6]:
        for y in "sudan":
            print(i,j,y)

i = 1
while(i<=10):
    print(i)
    i += 1

a = [1,2,3,4,5]
l = len(a)
while(l!=0):
    print(a[l-1])
    l -= 1

i = 1
while(i<=200):
    if i%2==0:
        print(i,'number is even')
        if i == 256:
            break
    i += 1

import random
random_num = random.randint(1,15)
print(random_num)
guess_count=[]
i=0
while True:
    user_input = int(input("Guess the number "))
    i += 1
    if random_num == user_input:
        print("Right")
        play_more = input("Do you want to play more? Y/N ").upper()
        if play_more == "Y":
            guess_count.append(i)
            random_num = random.randint(1,15)
            print("again ....",random_num)
            i=0
        else:
            guess_count.append(i)

            break

print(f"attempt: {i}")
print(f"history attempt: {guess_count}")
'''


Cor_Ps = 'secure123'
attempt = 0
while True:
    attempt += 1
    att_left = 4 - attempt
    Ps_Attempt = input("Enter Password: ")
    if Cor_Ps == Ps_Attempt:
        print("Password Successful")
        break
    else:
        print("Wrong Password!!")
        print(f"attempts left: {att_left}")
        if(att_left == 0):
            print("no attempts left")
            break






