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
    print(a[l])
    l -= 1

i = 1
while(i<=200):
    if i%2==0:
        print(i,'number is even')
        if i == 256:
            break
    i += 1






