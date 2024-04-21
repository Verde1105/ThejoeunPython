import os
import re
import pandas as pd

directory = "csse_covid_19_daily_reports"
file_pattern = r"(07-31-2021)|((08|09|10|11|12)-\d{2}-2021).csv"
file_pattern2= r"((01|02|03|04|05|06|07)-\d{2}-2022).csv"

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

# 결과 출력
print(df)
# print(df[153:154])
#(평균, 중앙값, 최빈값, 표준편차, 분산, 첨도, 왜도, 범위, 최소값,최대값, 합, 관측수)
df.dropna()
df.describe()#관측수 평균 표준편차 최소 최대
print('관측수 \n',df.loc[:,['확진자', '사망자']].count())#관측수
print('평균 \n',df.loc[:, ['확진자', '사망자']].mean()) #평균
print('표준편차 \n',df.loc[:, ['확진자', '사망자']].std()) #표준편차
print('최소 \n',df.loc[:, ['확진자', '사망자']].min()) #최소
print('최대 \n',df.loc[:, ['확진자', '사망자']].max()) #최대
print('합 \n',df.loc[:, ['확진자', '사망자']].sum()) #합
print('중앙값 \n',df.loc[:, ['확진자', '사망자']].median())#중앙값
print('최빈값 \n',df.loc[:, ['확진자', '사망자']].mode())#최빈값
print('분산 \n',df.loc[:, ['확진자', '사망자']].var())#분산
print('첨도 \n',df.loc[:, ['확진자', '사망자']].kurt())#첨도
print('왜도 \n',df.loc[:, ['확진자', '사망자']].skew())#왜도
print('범위 \n',df.loc[:, ['확진자', '사망자']].max() - df.loc[:, ['확진자', '사망자']].min())#범위

import numpy as np
import scipy.stats as sc
print('확진자 관측수 \n',np.array(df.loc[:,['확진자']].size))#관측수
print('사망자 관측수 \n',np.array(df.loc[:,['사망자']].size))#관측수
print('확진자 평균 \n',np.mean(df.loc[:,['확진자']])) #평균
print('사망자 평균 \n',np.mean(df.loc[:,['사망자']])) #평균
print('확진자 표준편차 \n',np.std(df.loc[:,['확진자']])) #표준편차
print('사망자 표준편차 \n',np.std(df.loc[:,['사망자']])) #표준편차
print('확진자 최소 \n',np.min(df.loc[:,['확진자']])) #최소
print('사망자 최소 \n',np.min(df.loc[:,['사망자']])) #최소
print('확진자 최대 \n',np.max(df.loc[:,['확진자']])) #최대
print('사망자 최대 \n',np.max(df.loc[:,['사망자']])) #최대
print('확진자 합 \n',np.sum(df.loc[:,['확진자']])) #합
print('사망자 합 \n',np.sum(df.loc[:,['사망자']])) #합
print('확진자 중앙값 \n',np.median(df.loc[:,['확진자']]))#중앙값
print('사망자 중앙값 \n',np.median(df.loc[:,['사망자']]))#중앙값
print('확진자 최빈값 \n',sc.mode(df.loc[:,['확진자']],keepdims=True))#최빈값
print('사망자 최빈값 \n',sc.mode(df.loc[:,['사망자']],keepdims=True))#최빈값
print('확진자 분산 \n',np.var(df.loc[:,['확진자']]))#분산
print('사망자 분산 \n',np.var(df.loc[:,['사망자']]))#분산
print('확진자 첨도 \n',sc.kurtosis(df.loc[:,['확진자']]))#첨도
print('사망자 첨도 \n',sc.kurtosis(df.loc[:,['사망자']]))#첨도
print('확진자 왜도 \n',sc.skew(df.loc[:,['확진자']]))#왜도
print('사망자 왜도 \n',sc.skew(df.loc[:,['사망자']]))#왜도
print('확진자 범위 \n',np.ptp(df.loc[:,['확진자']])) #범위 
print('사망자 범위 \n',np.ptp(df.loc[:,['사망자']])) #범위