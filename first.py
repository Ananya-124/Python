import random
def lucky():
    a=input("name")
    b=int(input("enter only date or month of your birthday"))
    e=a.capitalize()
    c=(random.randrange(0,b))
    d=c+1
    print("Hello",e,"Your lucky number is:",d)
lucky()