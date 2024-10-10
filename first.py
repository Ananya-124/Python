import random
def lucky():
    name=input("what is your name")
    dob=int(input("ente only birth date and month not year "))
    rad=(random.randrange(0,dob))
    
    print( name," your lucky number is" , rad )
lucky()
