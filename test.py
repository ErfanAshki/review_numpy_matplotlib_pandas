import matplotlib.pyplot as plt
import numpy as np

x1 = np.array((1,2,3))
y1 = np.array((6,5,4))
plt.subplot(1,2,1)
plt.plot(x1, y1)

x2 = np.array((0,3,6))
y2 = np.array((1,4,7))
plt.subplot(1,2,2)
plt.plot(x2, y2)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,10)
plt.ylim(0,10)
plt.title('subplot horizontal chart')
plt.legend()
plt.show()
