s='we have class on sunday'
l=[]
revl=[]
res=''
for val in s:
    if val==' ':
        l=[res]+l
        res=''
    else:
        res=val+res
l+=[res]
print(l)
for vv in l:
    revl=[vv]+revl
print(revl)
ind=0
rev=''
while ind!=len(revl):
    if ind!=len(revl)-1:
        rev=rev+revl[ind]+' '
    else:
        rev+=revl[ind]
    ind+=1
print(rev)
    

