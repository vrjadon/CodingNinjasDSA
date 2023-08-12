def bsFirstOccurence(li : [int],target : int):
    upper=0
    lower=len(li)-1
    while upper<=lower:
        middle=(upper+lower)//2
        print(upper)
        print(lower)
        print(middle)
        if target<li[middle]:
            upper=middle-1
        elif target>li[middle]:
            lower=middle+1
        elif target==li[middle]:
            while target==li[middle]:
                middle=middle-1
        print(middle)


n=6
li=[1,2,2,3,3,4]
x=2
bsFirstOccurence(li,x)