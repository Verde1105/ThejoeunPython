import numpy as np

array1 = np.arange(0,8).reshape(2,4)#reshape(2,4) = 2행 4열
array2 = np.arange(0,8).reshape(2,4)
array3 = np.concatenate([array1, array2], axis=0)#concatenate는 특정한 기준으로 두 표를 합할 수 있음

print(array3)

array1 = np.arange(0,8).reshape(2,4)
array2 = np.arange(0,8).reshape(2,4)
array3 = np.concatenate([array1, array2], axis=0)#concatenate는 특정한 기준으로 두 표를 합할 수 있음
array4 = np.arange(0,4).reshape(4,1)#4행 1열 이니 길쭉한 모양의 표가 나온다.

print(array3 + array4)

#넘파이는 서로 다른 형태의 배열도 연산 가능하게 해준다.
#reshape(4,1)으로 길쭉한 모양이었을 표를 정사각형 모양의 표화 합할려면, 부족한 부분만큼 값이 복사가 되어 형태를 맞춘다. 
#이것을 <<브로드캐스트>>라 한다.