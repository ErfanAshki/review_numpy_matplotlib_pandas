import numpy as np 

array1 = np.array([[[1,3],[5,7],['hi',6]] , [[4,4],['ll',0],[1,10]]])

for array in array1:
    for i in array:
        for a in i:
            print(a)
