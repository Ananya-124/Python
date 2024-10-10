import string
import random
def rand():
    a=''.join(random.choices(string.ascii_uppercase, string.punctuation,k=2))
   
    print(a)
rand()