userStr = input("Enter a string :")
myOutput=""
for x in range(0,len(userStr),2):
    myOutput += userStr[x]
else:
    print(myOutput)
