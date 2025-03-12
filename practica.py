numeros= [1,2,3,4,5]

total = sum(numeros)

print(total)

num = [23,5,89,12,37,4,95]

macT ,mincT= max(num),min(num)

print("minimo =>",macT)
print("minmo=>",mincT)

numT = [10,15,20,25,30,35,40]
numpra=[]
for i in numT:
    if (i % 2 == 0):
        numpra.append(i)

print(numpra)

dupl=[1,2,2,3,4,4,5]
newList=[]

for numTT in dupl:
    if numTT not in newList:
        newList.append(numTT)

print(newList)

newlisto=[]

[newlisto.append(x) for x in dupl if x not in newlisto]

print(newlisto)

newT = [1,3,3,4,5,6,7,8]

listNew = []
listImpar = []

[listNew.append(x) for x in newT if x not in listNew]

print(listNew)

[listImpar.append(x) for x in newT if x % 2 != 0 and x not in listImpar]

print(listImpar)




