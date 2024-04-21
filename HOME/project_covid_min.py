import pandas as pd
import os
import re

# 파일 경로 패턴
file_pattern = r"(08|09|10)-\d{2}-2021.csv"

# 검색할 디렉토리 경로
directory = "csse_covid_19_daily_reports"

# 데이터프레임 생성을 위한 빈 리스트
dataframes = [] # 전처리 담을 그릇

# 디렉토리 내의 파일 검색
for root, dirs, files in os.walk(directory): #root: 전체 경로 저장 (문자열), #dirs : 목록 (이름으로 저장) #file (파일로 저장)
    for file in files:  # 파일명이 패턴과 일치하는지 확인
        if re.match(file_pattern, file):
            file_path = os.path.join(root, file)  # 파일 경로를 리스트에 추가

            # CSV 파일 읽기
            covid_data = pd.read_csv(file_path)

            # 'Country_Region'이 'Korea, South'인 행 추출
            korea_south = covid_data[covid_data['Country_Region'] == 'Korea, South']

            # 발병자 수, 사망자 수 가져오기
            confirmed = korea_south['Confirmed'].values[0]
            deaths = korea_south['Deaths'].values[0]

            # 파일명에서 날짜 정보 추출
            date = korea_south['Last_Update'].values[0]
            date = pd.to_datetime(date).strftime('%Y-%m-%d') # 시간 값 제거

            # 데이터프레임 생성
            df = pd.DataFrame({'날짜': date, '국가': 'Korea', '발병자 수': confirmed, '사망자 수': deaths}, index=[0])

            # 데이터프레임을 리스트에 담기(추가)
            dataframes.append(df)

# 모든 데이터프레임을 합치기
covid_draft = pd.concat(dataframes, ignore_index=True)

print(covid_draft )

















