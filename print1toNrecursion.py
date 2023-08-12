
def sum1toN(n):
    if n==0:
        return 0
    return n+sum1toN(n-1)
n=int(input())
print(sum1toN(n))