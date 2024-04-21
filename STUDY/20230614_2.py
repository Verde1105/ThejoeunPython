import pandas as pd

df = pd.read_csv('data/scorse.csv')
df.head(3)

s_name = df['name']
s_name.head(3)

s_name.index

s_name.values

s_name.shape#열은 출력안됨

df['math'].head(3)

df_namekor = df[['name','kor']]
df_namekor.head(3)

df[['math']]#이러면 데이터 프레임 형태로 하나의 칼럼을 추출해준다(해당지문은 메스칼럼을 추출한것)
df_math = df[['math']]




