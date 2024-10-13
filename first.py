import numpy as np
speed = [20,30,40,50,60,70]
age = [1,2,3,4,5,5,6]
sd = np.std(speed)
print(int(sd))
print(int(np.var(age)))
print(np.percentile(speed,70))