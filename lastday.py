#map and filter
#map/filter(function, iterable)

def even(n):
    return n%2==0  

data = [1,2,3,4,5,6,7,8,9,10]

a = list(filter(even, data))
print(a)


list2 = [1,2,3,4,5,6,7,8,9]
def add_two(n):
    return n+2
map_data = list(map(add_two, list2))
print(map_data) 
