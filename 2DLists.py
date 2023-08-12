'''str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)'''
str=input().split()
n,m=int(str[0]),int(str[1])

arr=[[int(j) for j in input().split()] for i in range(n)]


def lar_col_sum(li):
    n=len(li)
    m=len(li[0])
    max_sum=-1
    max_sum_index=-1
    for j in range(m):
        sum=0
        for i in range(n):
            sum+=li[i][j]
        if sum>max_sum:
            max_sum_index=j
            max_sum=sum
    return max_sum,max_sum_index
print(lar_col_sum(arr))
