import random
import matplotlib.pyplot as plt
import numpy as np

print(random.randrange(1991, 2010, 10))

x = []

for i in range(1000):
    x.append(random.gauss(100,9))

#use hist gram to plot
plt.hist(x, range(200), histtype="bar", rwidth=0.8)
#plt.show()

#np.std(arr) to calculate standard deviation
print(np.std(x))
