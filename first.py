import random
def lucky():
    name=input("what is your name")
    dob=int(input("ente only birth date "))
    rad=(random.randrange(0,dob))
    length=len(name)
    
    print( name," your lucky number is" , (length + rad + 1) , "😊😊" )
lucky()
def letter():
    name=input("enter your name to get your future name")
    ran=(random.randrange('a','z'))
    print(ran)
letter()