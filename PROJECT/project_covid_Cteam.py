import os
import re
import pandas as pd
import numpy as np

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


        #2번 시작
        data1 = new_confirmed #확진자
        data2 = new_deaths #사망자


        #평균
        mean = pd.Series(data1).mean()
        print("평균:", mean)
        mean = np.mean(data2)
        print("평균:", mean)


        #중앙값
        median = pd.Series(data1).median()
        print("중앙값:", median)
        median = np.median(data2)

        #최빈값
        mode = pd.Series(data1).mode()
        print("최빈값:", mode)
        # 최빈값 계산
        def 사망자_최빈값(data2):
            unique_values, counts = np.unique(data2, return_counts=True)
            max_count_idx = np.argmax(counts)
            mode = unique_values[max_count_idx]
            return mode

        mode = 사망자_최빈값(data2)
        print("최빈값:", mode)


        #표준편차
        std = pd.Series(data1).std()
        print("표준편차:", std)
        std = np.std(data2)
        print("표준편차:", std)

        #분산
        var = pd.Series(data1).var()
        print("분산:", var)
        var = np.var(data2)
        print("분산:", var)

        #첨도
        kurtosis = pd.Series(data1).kurtosis()
        print("첨도:", kurtosis)
        #첨도 계산
        def 사망자_첨도계산(data2):
            mean = np.mean(data2)
            std = np.std(data2, ddof=0)
            kurtosis = np.mean((data2 - mean) ** 4) / (std ** 4)
            return kurtosis

        kurtosis_val = 사망자_첨도계산(data2)
        print("첨도:", kurtosis_val)


        #왜도
        skewness = pd.Series(data1).skew()
        print("왜도:", skewness)
        #왜도 계산
        def 사망자_왜도계산(data2):
            mean = np.mean(data2)
            std = np.std(data2, ddof=0)
            skewness = np.mean((data2 - mean) ** 3) / (std ** 3)
            return skewness

        skewness = 사망자_왜도계산(data2)
        print("왜도:", skewness)


        #범위
        range_val = pd.Series(data1).max() - pd.Series(data1).min()
        print("범위:", range_val)
        range_val = np.ptp(data2)
        print("범위:", range_val)

        #최소값
        min_val = pd.Series(data1).min()
        print("최소값:", min_val)
        min_val = np.min(data2)
        print("최소값:", min_val)


        #최대값
        max_val = pd.Series(data1).max()
        print("최대값:", max_val)
        max_val = np.max(data2)
        print("최대값:", max_val)


        #합
        sum_val = pd.Series(data1).sum()
        print("합:", sum_val)
        sum_val = np.sum(data2)
        print("합:", sum_val)


        #관측수
        count = pd.Series(data1).count()
        print("관측수:", count)
        count = len(data2)
        print("관측수:", count)

    # DataFrame 생성
    df = pd.DataFrame(data_list)

# 결과 출력
print(df)
# print(df[153:154])
