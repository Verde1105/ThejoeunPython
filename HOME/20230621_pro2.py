import pandas as pd

# 샘플 데이터 생성
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 평균
mean = pd.Series(data).mean()
print("평균:", mean)

# 중앙값
median = pd.Series(data).median()
print("중앙값:", median)

# 최빈값
mode = pd.Series(data).mode()
print("최빈값:", mode)

# 표준편차
std = pd.Series(data).std()
print("표준편차:", std)

# 분산
var = pd.Series(data).var()
print("분산:", var)

# 첨도
kurtosis = pd.Series(data).kurtosis()
print("첨도:", kurtosis)

# 왜도
skewness = pd.Series(data).skew()
print("왜도:", skewness)

# 범위
range_val = pd.Series(data).max() - pd.Series(data).min()
print("범위:", range_val)

# 최소값
min_val = pd.Series(data).min()
print("최소값:", min_val)

# 최대값
max_val = pd.Series(data).max()
print("최대값:", max_val)

# 합
sum_val = pd.Series(data).sum()
print("합:", sum_val)

# 관측수
count = pd.Series(data).count()
print("관측수:", count)