#************func def *************************
def isAmstrong(inptStr)->bool :
    stLen = len(inptStr)
    sum=0
    for digit in inptStr:
        sum += (int(digit)**stLen)
    else:
        if int(inptStr)==sum:
            return True
        else:
            return False

#*********End func def*************************

#ask user for number
userVal = input("Please enter numeric value to check :")
if isAmstrong(userVal):
    print(userVal," is an Amstrong number")
else:
    print(userVal," Is not an Amstrong number")
