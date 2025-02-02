import matplotlib.pyplot as plt
import numpy as np

x1 = np.array((1,2,3))
y1 = np.array((6,5,4))
plt.subplot(3,1,1)
plt.plot(x1, y1)

x2 = np.array((0,3,6))
y2 = np.array((1,4,7))
plt.subplot(3,1,2)
plt.plot(x2, y2)

x3 = np.array((2,9,1))
y3 = np.array((0,6,3))
plt.subplot(3,1,3)
plt.plot(x3, y3)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,10)
plt.ylim(0,10)
# plt.title('subplot horizontal chart')
plt.legend()
plt.show()
