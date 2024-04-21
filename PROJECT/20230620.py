import pandas as pd
import numpy as np
import os
import re

#(1) 1년동안 대한민국에서 발생한 코로나 발생자수 및 사망자 수 데이터 대상으로 전처리를 실시하시오.

#(2) 1년동안 대한민국에서 발생한 코로나 발생자수 및 사망자 수 데이터 대상으로 기술통계량(평균, 중앙값, 최빈값, 표준편차, 분산, 첨도, 왜도, 범위, 최소값,
#   최대값, 합, 관측수)을 2가지 이상의 방법(함수, 메서드)으로 계산하시오.

#(3) https://ncov.kdca.go.kr/ 에서 제공된 코로나 발생현황 자료의 수정본 csv 파일, 내 일별 발생자수와 사망자수와 (1)번에서 산출된 일별 발생자수와 사망
#   자수와 비교하여 통계량이 같은 지 확인하시오. 
#   만약 통계량이 다르다면 해당 날짜, 통계량의 리스트를 제시하시오.

"""
제출기한: 2023년 6월 28일(수) 09:30
제출처: 카페 내 ‘과제제출’ 게시판
제출물: 보고서, python 파일
제출양식: PPTX
발표: 모든 팀원이 발표

내 담당 : 2월~ 4월의 데이터
"""

folder_path = 'G:\Workspace\Thejoeun\PROJECT\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports'  #폴더 경로 지정
file_pattern = r"(02|03|04)-\d{2}-2022.csv"
file_list = os.listdir(folder_path)

corona19 = []  #CSV 파일의 데이터를 저장할 리스트

for file_name in file_list:
    if re.match(file_pattern, file_name):
        file_path = os.path.join(folder_path, file_name)

        df = pd.read_csv(file_path)  #판다스 형식으로 읽어오겠다, csv를.
        corona19.append(df)  # DataFrame을 리스트에 추가
        #column_names = df.columns.tolist()
        #print(column_names)

# 모든 파일에 대해 필터링 작업을 수행합니다
column_name = 'Country_Region'  # 수색할 칼럼의 이름
search_name = 'Korea, South'  # 키워드


filtered_data = []
for df in corona19:
    filtered_df = df[df[column_name] == search_name]
    filtered_df = filtered_df.loc[:, ['Last_Update','Confirmed', 'Deaths']]
#    filtered_df = filtered_df[filtered_df['Last_Update'].isin(file_pattern)]
    filtered_data.append(filtered_df)
    print(filtered_data)


# 모든 CSV 파일의 데이터를 하나의 DataFrame으로 합치거나 필요에 맞게 처리할 수 있습니다
# 예를 들어, 모든 CSV 파일의 행을 합친 후 numpy 배열로 변환하는 경우:
#combined_data = pd.concat(corona19, axis=0)  # 모든 DataFrame을 행으로 합칩니다
#numpy_array = combined_data.to_numpy()  # numpy 배열로 변환합니다





