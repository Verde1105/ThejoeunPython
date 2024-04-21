import pandas as pd
import numpy as np


df = pd.DataFrame({'float':[1.0, 2.0],
                   'int':[1 , 2],
                   'datetime':[pd.Timestamp('20200101'),pd.Timestamp('20210101')],
                   'string' : ['a','b'],
                   'bool':[True,False],
                   'object': [1,'-'],
                   'float2' : [1.0, 2]
                   })

#시리즈의 자료형 확인 법
df['int'].dtype#인트 칼럼 내용물 확인중

#숫자형과 문자형이 혼합되어 있는 경우의 자료형 확인법
type(df.loc[0,'object'])
print(df.loc[1,'object'])
print(type(df.loc[1,'object']))
#확인해보면 오브젝트 안에 각각 인트와 스트링으로 들어가 있다.












