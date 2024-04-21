import pandas as pd
import numpy as np

df = pd.DataFrame({'coll' : [1, 2],
                   'col2' : [3, 4],
                   'col3' : [5, '-']#col3는 혼합형이라 오브젝트 형으로 들어간다.
                   })


#오브젝트형인 col3 칼럼을 문자형으로 변환시키기
df['col3'] = df['col3'].astype('str')
type(df.loc[0,'col3'])
df['col3'] = df['col3'].astype('int')#이러면 인트형으로 바뀐다.


#변경할수 없는 자료가 섞여있으면 에러가 발생(쉼표나, 하이픈같은거)
#자료형이 혼합된 칼럼을, 숫자형으로 변환하는 법

#예시 데이터
s2 = pd.Series(['1.0', '2', -3, 'a'])

#기본형태, 이때는 에러발생하면, 에러를 띄워줌
pd.to_numeric(s2)

#숫자로 변경 불가능한 자료가 있으면 작업하지 않음.
pd.to_numeric(s2, errors='ignore')

#숫자로 변경 불가능한 값이 널값으로 변경.
pd.to_numeric(s2, errors='coerce')#숫자로 바뀌긴 하 되, 내용물 중 실수가 있었기 때문에 실수형태로 변한다.


#시계열 데이터로 변경
df1 = pd.read_csv('data/birth)die.csv')
df.head

#오브젝트이던 타입을, 에스타입으로, 데이트 타임 형태로 변환
df['출생'] = df['출생'].astype('datetime64')

#오브젝트이던 타입을, 투 데이트타임으로, 데이트 타임 형태 변환
df['사망'] = pd.to_datetime(df['사망'])



