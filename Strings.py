def replacechar(str,char1,char2):
    n=len(str)
    for i in range(n):
        if str[i]==char1:
            str=str.replace(char1,char2)
    return str
str="vishwas raj jadon"
s=replacechar(str,'a','x')
print(s)