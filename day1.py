lst5 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
i = int(input("enter the index value: "))
j = len(lst5)
if i<=j and i>-j:
    print(f"the index value of {i} is {lst5[i]}")
else:
    input(f"Please input valid index between {j} and {-j}")

#append
lst5.append(False)

lst5.insert(1, True)

#extend adds (a to b) or (b to a)
a = [1,2,3,4,5]
b = [10,11,12,13,14,15]
b.extend(a)
a.extend(b)


#concat
c = a+b
print(a,b)
print(c) 