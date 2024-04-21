import numpy as np

#집계함수!!

array = np.arange(16).reshape(4,4)

print("최대값:", np.max(array))#표 안에서 가장 큰 값이 나옴
print("최소값:", np.min(array))#표 안에서 가장 작은 값이 나옴
print("합계:", np.sum(array))
print("평균값:", np.mean(array))

#각각의 행이나 열을 기준으로 합계라던가 값을 구할 수도 있다.



