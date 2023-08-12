string='vishwas raj jadon is a thakur and jadon boy and also very smarty cute boy with a mad girlfriend'
s=string.split()
freq_dict={}
for i in s:
    if i in freq_dict:
        freq_dict[i]+=1
    else:
        freq_dict[i]=1
print(freq_dict)



