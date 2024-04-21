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



        #!!!!!
        # <<< 여기서부터 2번 문제 계산 시작>>>
        #!!!!!
        
        data1 = previous_confirmed  # 확진자
        data2 = previous_deaths  # 사망자

        # 평균
        mean = np.mean(data1)
        print("평균:", mean)
        mean = np.mean(data2)
        print("평균:", mean)


        # 중앙값
        median = np.median(data1)
        print("중앙값:", median)
        median = np.median(data2)
        print("중앙값:", median)


        # 최빈값
        def calculate_mode(data):
            unique_values, counts = np.unique(data, return_counts=True)
            max_count_idx = np.argmax(counts)
            mode = unique_values[max_count_idx]
            return mode

        mode = calculate_mode(data1)
        print("최빈값:", mode)
        mode = calculate_mode(data2)
        print("최빈값:", mode)


        # 표준편차
        std = np.std(data1)
        print("표준편차:", std)
        std = np.std(data2)
        print("표준편차:", std)


        # 분산
        var = np.var(data1)
        print("분산:", var)
        var = np.var(data2)
        print("분산:", var)


        # 첨도
        def calculate_kurtosis(data):
            mean = np.mean(data)
            std = np.std(data)
            kurtosis = np.mean((data - mean) ** 4) / (std ** 4)
            return kurtosis

        kurtosis_val = calculate_kurtosis(data1)
        print("첨도:", kurtosis_val)
        kurtosis_val = calculate_kurtosis(data2)
        print("첨도:", kurtosis_val)


        # 왜도
        def calculate_skewness(data):
            mean = np.mean(data)
            std = np.std(data)
            skewness = np.mean((data - mean) ** 3) / (std ** 3)
            return skewness

        skewness = calculate_skewness(data1)
        print("왜도:", skewness)
        skewness = calculate_skewness(data2)
        print("왜도:", skewness)


        # 범위
        range_val = np.ptp(data1)
        print("범위:", range_val)
        range_val = np.ptp(data2)
        print("범위:", range_val)


        # 최소값
        min_val = np.min(data1)
        print("최소값:", min_val)
        min_val = np.min(data2)
        print("최소값:", min_val)


        # 최대값
        max_val = np.max(data1)
        print("최대값:", max_val)
        max_val = np.max(data2)
        print("최대값:", max_val)


        # 합
        sum_val = np.sum(data1)
        print("합:", sum_val)
        sum_val = np.sum(data2)
        print("합:", sum_val)


        # 관측수
        count = len(data1)
        print("관측수:", count)
        count = len(data2)
        print("관측수:", count)

# DataFrame 생성
df = pd.DataFrame(data_list)

# 결과 출력
print(df)