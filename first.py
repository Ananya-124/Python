import random
 
def lucky():
    a=input("name")
    a[0].upper() + a[1:]
    b=int(input("enter only date or month of your birthday"))
    c=(random.randrange(0,b))
    d=c+1
    print("Hello", a, "Your lucky number is:",d)
    print(a)
   
lucky()