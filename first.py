import random
def whoPay(names):
    
    b=len(names)
    c=(random.randrange(0,b))
    print(names[c]," should pay the bill")
    print(c)
   
names=["a","b","c","d","e","f"]
whoPay(names)

