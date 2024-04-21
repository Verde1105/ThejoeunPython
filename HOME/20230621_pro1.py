import numpy as np

# 샘플 데이터 생성
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 평균
mean = np.mean(data)
print("평균:", mean)

# 중앙값
median = np.median(data)
print("중앙값:", median)

# 표준편차
std = np.std(data)
print("표준편차:", std)

# 분산
var = np.var(data)
print("분산:", var)

# 범위
range_val = np.ptp(data)
print("범위:", range_val)

# 최소값
min_val = np.min(data)
print("최소값:", min_val)

# 최대값
max_val = np.max(data)
print("최대값:", max_val)

# 합
sum_val = np.sum(data)
print("합:", sum_val)

# 관측수
count = len(data)
print("관측수:", count)