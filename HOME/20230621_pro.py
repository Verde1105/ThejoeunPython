import numpy as np
import pandas as pd

# 샘플 데이터 생성
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 평균
mean = np.mean(data)
print("평균:", mean)

# 중앙값
median = np.median(data)
print("중앙값:", median)

# 최빈값
mode = pd.Series(data).mode()
print("최빈값:", mode)

# 표준편차
std = np.std(data)
print("표준편차:", std)

# 분산
var = np.var(data)
print("분산:", var)

# 첨도
kurtosis = pd.Series(data).kurtosis()
print("첨도:", kurtosis)

# 왜도
skewness = pd.Series(data).skew()
print("왜도:", skewness)

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


"""
평균 (Mean):

평균은 데이터의 총합을 데이터의 개수로 나눈 값입니다.
데이터의 중심 경향성을 나타내며, 주로 연속형 데이터에 사용됩니다.
예를 들어, 1, 2, 3, 4, 5라는 데이터가 있다면, 평균은 (1 + 2 + 3 + 4 + 5) / 5 = 3입니다.
중앙값 (Median):

중앙값은 데이터를 크기순으로 정렬했을 때 가운데에 위치한 값입니다.
이상치(outlier)에 덜 영향을 받는 강건한(robust) 통계량입니다.
예를 들어, 1, 2, 3, 4, 5라는 데이터가 있다면, 중앙값은 3입니다.
최빈값 (Mode):

최빈값은 데이터에서 가장 자주 나타나는 값입니다.
범주형 데이터에서 주로 사용되며, 여러 개의 최빈값이 있을 수 있습니다.
예를 들어, 1, 2, 2, 3, 4, 4, 4, 5라는 데이터가 있다면, 최빈값은 4입니다.
표준편차 (Standard Deviation):

표준편차는 데이터의 퍼짐 정도를 나타내는 값으로, 평균과의 차이의 제곱의 평균의 양의 제곱근입니다.
데이터의 변동성을 나타내며, 값이 클수록 데이터가 평균에서 멀리 퍼져있다는 의미입니다.
분산 (Variance):

분산은 데이터의 퍼짐 정도를 나타내는 값으로, 평균과의 차이의 제곱의 평균입니다.
표준편차의 제곱과 동일한 개념입니다.
표준편차보다는 값이 큰 특징을 가지고 있습니다.
첨도 (Kurtosis):

첨도는 데이터 분포의 꼬리 부분의 상대적인 비중을 나타내는 지표입니다.
정규분포와 비교하여 꼬리 부분의 뾰족함을 측정합니다.
첨도가 0보다 크면 정규분포보다 뾰족한 분포, 0보다 작으면 정규분포보다 완만한
"""