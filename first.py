def isprime():
    num=int(input("enter a number"))
    if num<2:
        return False
    for i in range(2, num+1):
        if num%i==0:
            return False
        else:
            return True

