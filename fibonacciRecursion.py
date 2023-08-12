def fibonacciN(n):
    if n==1 or n==2:
        return 1
    return fibonacciN(n-1)+fibonacciN(n-2)
   
    


n=int(input())
print(fibonacciN(n))