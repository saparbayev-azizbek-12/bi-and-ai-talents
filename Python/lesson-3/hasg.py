mylist = [1,2,3,4,5,6,3,3,3,4,4,4,4]
ddict = {}
for i in mylist:
    ddict[i] = ddict.get(i,0) + 1
print(max(ddict,key=lambda x:ddict[x]))