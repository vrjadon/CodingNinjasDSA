def reverselist(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[length-i-1]=li[length-i-1],li[i]



li=[1,2,3,4,5,6]
reverselist(li)
print(li)