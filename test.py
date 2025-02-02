import matplotlib.pyplot as plt
import numpy as np


def create_plot(option):
    x = np.arange(-20,20,1)
    if option == 'daraje1':
        y = x
    elif option == 'daraje2':
        y = x ** 2
    elif option == 'daraje3':
        y = x ** 3
    elif option == 'daraje4':
        y = x ** 4
    return x , y 

x , y = create_plot('daraje1')
plt.subplot(2,2,1)
plt.plot(x,y,color='red')
plt.title('daraje1')
x , y = create_plot('daraje2')
plt.subplot(2,2,2)
plt.plot(x,y,color='blue')
plt.title('daraje2')
x , y = create_plot('daraje3')
plt.subplot(2,2,3)
plt.plot(x,y,color='green')
plt.title('daraje3')
x , y = create_plot('daraje4')
plt.subplot(2,2,4)
plt.plot(x,y,color='purple')
plt.title('daraje4')
plt.show()

