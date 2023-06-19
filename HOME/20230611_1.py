import numpy as np

#넘파이 사용법 기록

list_data = [1, 2, 3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)


array1 = np.arange(4)
print(array1)


array2 = np.zeros((4,4), dtype=float)#0으로 끝나는 실수로 이루어진 4x4의 2차원 배열
print(array2)

array3 = np.ones((3,3), dtype=str)#문자형식으로 된 3x3의 2차원 배열
print(array3)


array4 = np.random.randint(0,10,(3,3))#0~9까지 랜덤하게 초기화 된 배열 만들기 사이즈는 3x3
print(array4)

array5 = np.random.normal(0,1,(3,3))#평균이 0이고 표준편차가 1인 표준 정규를 띄는 배열


array11 = np.array([1,2,3])
array12 = np.array([4,5,6])
array13 = np.concatenate([array11, array12])

print(array13.shape)
print(array13)

array14 = np.array([1,2,3,4])
array15 = array14.reshape((2,2))
print(array15)

array16 = np.arange(4).reshape(2,4)
array17 = np.arange(4).reshape(2,4)
array18 = np.concatenate([array16, array17],axis=0)
print(array18)


array19 = np.arange(8).reshape(2,4)
left,rigft =np.split(array19, [2], axis=1)
print(left.shape)
print(rigft.shape)
print(array19)


