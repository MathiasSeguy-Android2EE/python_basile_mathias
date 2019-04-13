#IsToto

def isToto(name):
    # print("Instead of comparing "+name+" let's compare "+name.lower())
    if "toto" in name.lower() :
        print (name+" Il s'apelle toto")
    else:
        print (name+" C'est pas toto")

def testIsToto():
    isToto("John")
    isToto("toto")
    isToto("Toto")
    isToto("tOto")
    isToto("tOtO")
    isToto("tata")

#Ask Question
nameToCheck=input("Quel est le nom que tu veux comparer ?")
isToto(nameToCheck)