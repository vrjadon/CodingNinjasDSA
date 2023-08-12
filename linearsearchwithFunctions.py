def linearSearch(li,ele):
    for i in range(len(li)):
        if ele==li[i]:
            return i
    return -1
    
        

li=[int(x) for x in input().split()]
ele=int(input())
x=linearSearch(li,ele)
print(x)