import pandas as pd
import numpy as np

#

#샘플 데이터 생성
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#평균
mean = pd.Series(data).mean()
print("평균:", mean)
mean = np.mean(data)
print("평균:", mean)


#중앙값
median = pd.Series(data).median()
print("중앙값:", median)
median = np.median(data)

#최빈값
mode = pd.Series(data).mode()
print("최빈값:", mode)
# 최빈값 계산
def calculate_mode(data):
    unique_values, counts = np.unique(data, return_counts=True)
    max_count_idx = np.argmax(counts)
    mode = unique_values[max_count_idx]
    return mode

mode = calculate_mode(data)
print("최빈값:", mode)


#표준편차
std = pd.Series(data).std()
print("표준편차:", std)
std = np.std(data)
print("표준편차:", std)

#분산
var = pd.Series(data).var()
print("분산:", var)
var = np.var(data)
print("분산:", var)

#첨도
kurtosis = pd.Series(data).kurtosis()
print("첨도:", kurtosis)
#첨도 계산
def calculate_kurtosis(data):
    mean = np.mean(data)
    std = np.std(data, ddof=0)
    kurtosis = np.mean((data - mean) ** 4) / (std ** 4)
    return kurtosis

kurtosis_val = calculate_kurtosis(data)
print("첨도:", kurtosis_val)


#왜도
skewness = pd.Series(data).skew()
print("왜도:", skewness)
#왜도 계산
def calculate_skewness(data):
    mean = np.mean(data)
    std = np.std(data, ddof=0)
    skewness = np.mean((data - mean) ** 3) / (std ** 3)
    return skewness

skewness = calculate_skewness(data)
print("왜도:", skewness)


#범위
range_val = pd.Series(data).max() - pd.Series(data).min()
print("범위:", range_val)
range_val = np.ptp(data)
print("범위:", range_val)

#최소값
min_val = pd.Series(data).min()
print("최소값:", min_val)
min_val = np.min(data)
print("최소값:", min_val)


#최대값
max_val = pd.Series(data).max()
print("최대값:", max_val)
max_val = np.max(data)
print("최대값:", max_val)


#합
sum_val = pd.Series(data).sum()
print("합:", sum_val)
sum_val = np.sum(data)
print("합:", sum_val)


#관측수
count = pd.Series(data).count()
print("관측수:", count)
count = len(data)
print("관측수:", count)












