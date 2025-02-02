import matplotlib.pyplot as plt


x = [1,3,5,7]
height = [10,20,30,40]

plt.bar(x, height, width=0.5, color=['red','blue','green','yellow'], label='bar1')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('bar chart')
plt.show()
