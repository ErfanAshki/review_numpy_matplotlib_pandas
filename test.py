import numpy as np 

np_array1 = np.array([-8,0,3,14])
np_array2 = np.array((10,20,30,40))
new_array = np_array1[: , np.newaxis]   

print(new_array + np_array2)
    