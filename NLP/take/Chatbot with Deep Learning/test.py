
val=4
binVal=list(bin(val).replace("0b", ""))

# print(binVal.isdigit())


count=0
while (int(''.join(binVal)) != 0):
    count+=1
    for i in range(len(binVal)):
        if (i+1 > len(binVal)+1 ):
            if (binVal[i+1] == '0'):
                binVal[i]='1'
                continue
            elif (binVal[len(binVal)]=='1'):
                binVal[len(binVal[i])]='0'
                continue
print(count)
        
            



# print(binVal.isnumeric)


# n=5
# space=[1,2,3,1,2]
# x=1


# globalMinima=[]
# for i in range(len(space)-1):
#     tempList=space[i:i+x]

#     if (len(tempList) != x):
#         continue
    
#     print(tempList)
#     minVal=min(tempList)
#     globalMinima.append(minVal)

# print(max(globalMinima))

