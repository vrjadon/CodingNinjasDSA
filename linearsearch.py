isFound=False
li=[int(x) for x in input().split()]
print(li)
num=int(input())
for i in range(len(li)):
    if num==li[i]:
        print(i)
        isFound=True
        break
if isFound==False:
    print(-1)
    
    