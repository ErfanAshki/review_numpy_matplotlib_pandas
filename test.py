import matplotlib.pyplot as plt
import numpy as np

x1 = [1,4,5,3,5]
y1 = [2,5,2,6,7]
sizes = [10,50,5,200,100]
plt.scatter(x1, y1, s=sizes, label='point 1', color='green', marker='o')

x2 = [0,5,7,3]
y2 = [2,0,9,3]
plt.scatter(x2, y2, s=40, label='point 2', color='red', marker='*')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,10)
plt.ylim(0,10)
plt.title('scatter chart')
plt.legend()
plt.show()
