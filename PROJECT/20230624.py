import os
import re
import pandas as pd
import numpy as np

#경로설정하는 곳 = directory << 파일 실행 전, 반드시 자신에게 맞는 경로로 설정 바람
directory = "E:\Workspace\Thejoeun\PROJECT\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports"
file_pattern = r"(07-31-2021)|((08|09|10|11|12)-\d{2}-2021).csv"
file_pattern2 = r"((01|02|03|04|05|06|07)-\d{2}-2022).csv"

# 해당 패턴에 맞는 파일 경로 가져오기
file_paths2021 = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if re.match(file_pattern, file_name)]
file_paths2022 = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if re.match(file_pattern2, file_name)]
data_list = []
file_paths = file_paths2021 + file_paths2022
previous_confirmed = None
previous_deaths = None

for file_path in file_paths:
    # CSV 파일 이름에서 날짜 정보 추출
    date = re.search(r"(\d{2}-\d{2}-\d{4})", file_path).group(1)
    date = pd.to_datetime(date, format='%m-%d-%Y').strftime('%Y-%m-%d')

    # CSV 파일 읽어오기
    covid_data = pd.read_csv(file_path)

    # 'Country_Region'이 'Korea, South'인 행 추출
    korea_south = covid_data[covid_data['Country_Region'] == 'Korea, South']

    if not korea_south.empty:
        # 발병자 수, 사망자 수 가져오기
        confirmed = korea_south['Confirmed'].values[0]
        deaths = korea_south['Deaths'].values[0]

        # 전날의 발병자 수와 사망자 수가 이전 값과 다를 경우에만 저장
        if previous_confirmed is not None and previous_deaths is not None:
            new_confirmed = confirmed - previous_confirmed
            new_deaths = deaths - previous_deaths

            # 정보 리스트에 저장
            data_list.append({
                '날짜': date,
                '확진자': new_confirmed,
                '사망자': new_deaths
            })

        # 전날 발병자 수와 사망자 수 갱신
        previous_confirmed = confirmed
        previous_deaths = deaths

# DataFrame 생성
df = pd.DataFrame(data_list)

# 확진자 통계량 계산
mean_confirmed = df['확진자'].mean()
median_confirmed = df['확진자'].median()
mode_confirmed = df['확진자'].mode().values[0]
std_confirmed = df['확진자'].std()
var_confirmed = df['확진자'].var()
kurtosis_confirmed = df['확진자'].kurtosis()
skewness_confirmed = df['확진자'].skew()
range_confirmed = df['확진자'].max() - df['확진자'].min()
min_confirmed = df['확진자'].min()
max_confirmed = df['확진자'].max()
sum_confirmed = df['확진자'].sum()
count_confirmed = len(df['확진자'])

# 사망자 통계량 계산
mean_deaths = df['사망자'].mean()
median_deaths = df['사망자'].median()
mode_deaths = df['사망자'].mode().values[0]
std_deaths = df['사망자'].std()
var_deaths = df['사망자'].var()
kurtosis_deaths = df['사망자'].kurtosis()
skewness_deaths = df['사망자'].skew()
range_deaths = df['사망자'].max() - df['사망자'].min()
min_deaths = df['사망자'].min()
max_deaths = df['사망자'].max()
sum_deaths = df['사망자'].sum()
count_deaths = len(df['사망자'])

# 결과 출력
print("확진자 평균:", mean_confirmed)
print("확진자 중앙값:", median_confirmed)
print("확진자 최빈값:", mode_confirmed)
print("확진자 표준편차:", std_confirmed)
print("확진자 분산:", var_confirmed)
print("확진자 첨도:", kurtosis_confirmed)
print("확진자 왜도:", skewness_confirmed)
print("확진자 범위:", range_confirmed)
print("확진자 최소값:", min_confirmed)
print("확진자 최대값:", max_confirmed)
print("확진자 합:", sum_confirmed)
print("확진자 관측수:", count_confirmed)

print("사망자 평균:", mean_deaths)
print("사망자 중앙값:", median_deaths)
print("사망자 최빈값:", mode_deaths)
print("사망자 표준편차:", std_deaths)
print("사망자 분산:", var_deaths)
print("사망자 첨도:", kurtosis_deaths)
print("사망자 왜도:", skewness_deaths)
print("사망자 범위:", range_deaths)
print("사망자 최소값:", min_deaths)
print("사망자 최대값:", max_deaths)
print("사망자 합:", sum_deaths)
print("사망자 관측수:", count_deaths)