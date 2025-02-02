import matplotlib.pyplot as plt


x1 = [-2,0,4]
y1 = [0,3,6]
plt.plot(x1,y1, label='line1', linestyle='solid', color='green', linewidth=1, marker='o', markerfacecolor='yellow', markersize='8')

x2 = [2,5,6]
y2 = [1,4,3]
plt.plot(x2,y2, label='line2', linestyle='dashed', color='blue', linewidth=3, marker='o', markerfacecolor='yellow', markersize='6')

x3 = [3,0,-1]
y3 = [0,1,3]
plt.plot(x3,y3, label='line3', linestyle='dotted', color='red', linewidth=5, marker='o', markerfacecolor='yellow', markersize='4')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Three barometer')
plt.legend()

plt.show()
