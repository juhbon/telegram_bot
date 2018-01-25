import matplotlib.pyplot as plt
from math import sin,cos

x = [i for i in range(0,150)]
y = [sin(x) for x in x]
z = [cos(x) for x in x]

plt.plot(x,y)
plt.show()
plt.plot(x,z)
plt.show()
