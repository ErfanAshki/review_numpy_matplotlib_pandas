import matplotlib.pyplot as plt
import numpy as np

x = [1,4,5,3,5]
y = [2,5,2,6,7]
sizes = [10,50,5,200,100]

plt.scatter(x, y, s=sizes, label='point', color='green', marker='o')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(0,10)
plt.ylim(0,10)
plt.title('scatter chart')
plt.legend()
plt.show()
