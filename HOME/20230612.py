import numpy as np

array = np.random.randint(1, 10, size = 4).reshape(2,2)
print(array)

result_array = array * 10
print(result_array)

array1 = np.arange(4).reshape(2,2)
array2= np.arange(2)

array3 = array1+ array2

print(array3)