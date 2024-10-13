import numpy as np
import matplotlib.pyplot as plt
x=np.array([20,40])
y=np.array([10,30])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("HEALTH",font1)
plt.plot(x,y,'o',linestyle="dotted")
plt.xlabel("fruits",font1)
plt.ylabel("price",font2)

plt.show()