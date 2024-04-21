import pandas as pd

#데이터 프레임을 그룹화하여 그룹별 데이터 집계하기


df = pd.read_csv('data/titanic.csv')
df = df[['survivend', 'pclass','sex','age','embarked']]
df = df.dropna()
df.head()

len(df)

df1 = df.groupby('pclass').survivend.count().to_frame()
#객실 등급별 승선자 수를 구하고, 그 결과를 데이터 프레임1로 따로 저장.

df2 = df.groupby('pclass').survivend.sum().to_frame()
#객실 등급별 생존자 수를 구하고, 그 결과를 데이터 프레임2로 따로 저장.

df3 = df.groupby('pclass').survivend.mean().to_frame()
#객실 등급별 생존율을 구하고, 그 결과를 데이터 프레임3로 따로 저장.

df4 = pd.concat([df1,df2,df3], axis=1)
df4.columns = ['승선자수', '생존자수', '생존율']
df4
#객실등급별 탑승자수, 생존자수, 생존율 데이터프레임을 df4로 만들기

df5 = df.groupby('sex').survivend.count().to_frame()
df5
#성별에 따른 승선자 수, 데이터 프레임을 df5로 만들기

df6 = df.groupby('sex').survivend.sum().to_frame()
df6
#성별에 따른 생존자 수, 데이터 프레임을 df6로 만들기

df7 = df.groupby('sex').survivend.mean().to_frame()
df7
#성별에 따른 생존율을 데이터 프레임을 df7로 만들기

df8 = pd.concat([df5,df6,df7], axis=1)#얘네 묶어주세요!
df8.columns = ['승선자수', '생존자수', '생존율']#컬럼명 변겅중
df8
#객실등급별 탑승자수, 생존자수, 생존율 데이터프레임을 df8로 만들기


df.groupby(['sex','pclass']).survivend.mean()
#객실, 성별 별 생존율
#이렇게 쓰면 한번에 두가지 그룹의 결과값을 얻을 수 있다.

def my_mean(values):
    return sum(values)/len(values)
#그룹에 사용자 정의 함수 적용하기.

df.groupby(['sex','pclass']).survivend.agg(my_mean)
#agg(사용자정의함수명) 이러면 사용자 정의 함수를 쓸 수 있다.


#그룹 오브젝트 출력하기!
df20 = df[:20]
df20.head()
len(df20)

df20.groupby('pclass').groups
#이렇게 했을 시, pclass해당 칼럼 내, 같은 값을 가진 데이터 끼리 그룹으로 묶어서 출력해준다. 예를들어 1등석끼리, 2등석끼리.
#그룹별 인덱스

df20.groupby('pclass').get_group(1)
#pclass 해당 칼럼 안의 1의 데이터를 지닌 애들만 출력.




