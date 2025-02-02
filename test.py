import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0,4 * (np.pi) , 0.1)
y1 = np.sin(x1)
plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.title('Barometer 1')

x2 = np.arange(0,4 * (np.pi) , 0.5)
y2 = np.sin(x2)
plt.subplot(2,2,2)
plt.plot(x2,y2)
plt.title('Barometer 2')

x3 = np.arange(0,4 * (np.pi) , 1)
y3 = np.sin(x3)
plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.title('Barometer 3')

x4 = np.arange(0,4 * (np.pi) , 2)
y4 = np.sin(x4)
plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.title('Barometer 4')

plt.suptitle('COS(X)')
plt.show()
