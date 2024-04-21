import pandas as pd
import numpy as np

#결측치222

df = pd.read_csv('data/scorse.csv')
df.head()


#결측치 확인
df.isnull().sum()

#결측치 전부 0으로 채우기
df.fillna(0) #역시 저장할려면 소괄호 안에 같이 , 인플레이스 = 트루를 해줘야한다.








