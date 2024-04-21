import numpy as np
#<마스킹 연산!>

array1 = np.arange(16).reshape(4,4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2]

#이미지 올렸을때 쨍하거나 안맞는 픽셀들을 찾아 다른 타일로 바꿔버릴수도있음