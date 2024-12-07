#original list given
brands = ["Hermes", "Gucci", "Chanel", "Gucci",
           "Louis Vuitton", "Hermes", "Chanel","hugo boss", 
           "Guess", "Gucci", "Louis Vuitton"]

print(brands) #console guide... if debug....

brand_Set = set(brands) #convert to set so we loose duplicates.
print("Set now has :") #console guide...
print(brand_Set)

myDict = dict()
for brandname in brand_Set:
    myDict[brandname[0]] = brandname
else:
    print("finally Finished")               #just for my command line debugging steps tracking. can be commented out
    print("my Dict contents :",myDict)

#or if we are accoounting for diff brands with same first letters then.. 
myDict = dict()
for brandname in brand_Set:
    print(brandname) #console guide.... 
    if brandname[0] in myDict.keys():       #Check if we already have a key with this first letter
        myDict[brandname[0]].add(brandname)
    else:
        myDict[brandname[0]] = set()        #create dict value as an empty set, so we can account for diff brands with the same first letter
        myDict[brandname[0]].add(brandname)
else:
    print("finally Finished")               #just for my command line debugging steps tracking. can be commented out
    print("my Dict contents :",myDict)