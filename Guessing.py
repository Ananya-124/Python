import random
ip=int(input("please enter the range so you can guess the number b/w that range of numbers"))
gr=(random.randrange(ip))
print("Are You Ready To Guess?!")
chances=7
gc=0
while gc < chances:
    gc+=1
    mg = int(input("Please Enter Your Guess: "))
    if mg == gr:
        print("Hurray Your guess is right!!!")
        break
    elif gc >= chances and mg != gr:
        print(f'Oops sorry, The number is {gr} better luck next time')
    elif mg < gr:
        print("Your Guess is less than the number")
        
        
    elif mg > gr:
        print("Your Guess is more than the number")
        
        
    