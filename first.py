def isprime():
    
    num=int(input("enter a number"))
    if num<2:
        print("not a prime")
    for i in range(2, num+1):
        if num%i==0:
            print("not a prime")
        else:
            print("prime")

isprime()