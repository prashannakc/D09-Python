

def fibo(n):
    if n==1 or n==0:
        return n
    else:
        return n*fibo(n-1)
    
print(fibo(5))