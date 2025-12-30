'''
#a = tuple(stores all arguemnts) (args = arguments)
def test(*args):
    print(args)

test(1,2,3,4,5)
test(1,2,3)
test(1,2,3,4,5,7,7)
test()


def add(*num):
    sum = 0
    for i in num:
        sum += i
    return sum
result = add(4, 5, 6)
print(result)
'''


#CA - Average of Numeric Args
def average(*args):
    num = 0
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
            num += 1
            total += i
    return total/num
print(average("Prashanna", "KC", 1, 2, 3, 4.05))


    

    
