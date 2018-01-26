import matplotlib.pyplot as plt
from math import sin,cos

x = [i/250 for i in range(0,10000)]
y = [sin(x) for x in x]
z = [cos(x) for x in x]

figs = plt.figure() # Creating a window
window = figs.add_subplot(2,1,1) # Adding upper
window.set_xlabel('$x$') 
window.set_ylabel("$\sin(x)$")
window.set_title("I like $\pi$")
window.plot(x,y) # plot of sine
window = figs.add_subplot(2,1,2) # Addind lower plot
window.set_xlabel('$x$') 
window.set_ylabel("$\cos(x)$")
window.set_title("I like $\pi$")
window.plot(x,z) # plot of cosine
figs.show()

fig = plt.figure()
window = fig.add_subplot(1,1,1, aspect='equal') # Adding another plot
window.set_xlabel('$y$')
window.set_ylabel('$z$')
window.set_title('I like circles')
window.plot(y,z, label='sine+cosine')
fig.show()
