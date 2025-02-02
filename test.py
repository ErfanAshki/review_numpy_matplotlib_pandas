import matplotlib.pyplot as plt
import numpy as np


sizes = [2,4,6,8]
parts = ['training','eating','studying','sleeping']
my_explode = [0,0.05,0.1,0.15]
colors = ['green','red','blue','purple']

plt.pie(sizes, labels=parts, colors=colors, explode=my_explode, shadow=True, autopct='%1.1f%%')
plt.legend(title='four exercise')
plt.show()
