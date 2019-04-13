#IsToto

def isSameName(nameInitial,nameToCompare):
    # print("Instead of comparing "+name+" let's compare "+name.lower())
    if nameInitial.lower() in nameToCompare.lower() and nameToCompare.lower() in nameInitial.lower():
        print (nameToCompare+": Il s'apelle "+nameInitial)
    else:
        print (nameToCompare+": C'est pas "+nameInitial)


def isToto(name):
    isSameName("toTo",name)

def isTotoro(name):
    isSameName("toToro",name)

def isMathias(name):
    isSameName("mathias",name)

def isBasile(name):
    isSameName("basile",name)

def testIsToto():
    isToto("John")
    isToto("toto")
    isToto("Toto")
    isToto("tOto")
    isToto("tOtO")
    isToto("tata")

#Ask Question
keepAsking=True
while(keepAsking):
    nameToCheck=input("Quel est le nom que tu veux comparer (or quit) ? ")
    if("quit" in nameToCheck):
        keepAsking=False
    else:
        isToto(nameToCheck)
        isTotoro(nameToCheck)
        isMathias(nameToCheck)
        isBasile(nameToCheck)