import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
my_marks = [20,18,15,17]
your_marks = [18,14,20,17]
bar_width = 0.2

p1 = plt.bar(x, my_marks, bar_width, color='red', label='my marks')
p2 = plt.bar(x + bar_width, your_marks, bar_width, color='blue', label='your marks')

plt.xlabel('subjects')
plt.ylabel('scores')
plt.title('bar chart scores')
plt.xticks(x + (bar_width/2) , ('English','Sport','Math','Science'))
plt.legend()
plt.show()
