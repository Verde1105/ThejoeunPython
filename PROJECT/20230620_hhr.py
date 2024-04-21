import os
import pandas as pd

folder_path = 'G:\Workspace\Thejoeun\PROJECT\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports'  #폴더 경로 지정

file_list = os.listdir(folder_path)

corona19 = []  #CSV 파일의 데이터를 저장할 리스트

for file_name in file_list:
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)

        df = pd.read_csv(file_path)  #판다스 형식으로 읽어오겠다, csv를.
        corona19.append(df)  #DataFrame을 리스트에 추가


column_name = 'Country_Region'  #수색할 칼럼의 이름
search_name = 'Korea, South'  #키워드
search_month = ['2022-02', '2022-03', '2022-04']  #수색할 년-월 리스트

filtered_data = []
for df in corona19:
    column_names = df.columns.tolist() #수색할 칼럼명을 csv파일 칼럼명 리스트와 비교
    if column_name in column_names: #이름이 존재 하는지 여부를 찾는 !!!
        filtered_df = df[df[column_name] == search_name]
        filtered_df = filtered_df.loc[:, ['Last_Update', 'Confirmed', 'Deaths']]
        filtered_df['Last_Update'] = pd.to_datetime(filtered_df['Last_Update'])
        filtered_df = filtered_df[filtered_df['Last_Update'].dt.strftime('%Y-%m').isin(search_month)]
        filtered_data.append(filtered_df)

#출력부
result_df = pd.concat(filtered_data) #병합 !!
print(result_df.to_string(index=False)) #할당