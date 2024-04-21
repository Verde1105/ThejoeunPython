import pandas as pd

#데이터 프레임 연결하기
#인덱스 기준으로 연결

df1 = pd.DataFrame([['a', 1],['b', 2]],columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3],['d', 4]],columns=['letter', 'number'])
df3 = pd.DataFrame([['e', 5, '!'],['f',4, "@"]],columns=['letter', 'number', 'etc'])

df_rowconcat = pd.concat([df1,df2,df3])#연결 완료 + df_rowconcat새로운 칼럼을 만들어, 합한것을 담기까지 함.
df_rowconcat


#inner 공통된 컬럼만 남기기.
df_rowconcat = pd.concat([df1,df2,df3], join = 'inner')
df_rowconcat = pd.concat([df1,df2,df3], join = 'inner', ignore_index=True)#얘까지 추가하면, 인덱스 순번 정리까지 해줌.

df_rowconcat.loc


#열(인덱스)로 변결하기

df4 = pd.DataFrame({'age':[20,21,22]}, index= ['amy', 'james', 'david'])
df5 = pd.DataFrame({'phone':['010-111-1111', '010-222-2222', '010-333-3333']}, index= ['amy', 'james', 'david'])
df6 = pd.DataFrame({'job':['student', 'programer', 'ceo', 'designer']}, index= ['amy', 'james', 'david','j'])

pd.concat([df4,df5,df6])# 이렇게만 하면 행으로 붙기 때문에
pd.concat([df4,df5,df6], axis=1)#열로 붙을 수 있도록 추가해야함.

df_column_concat = pd.concat([df4,df5,df6], axis=1)#새 그릇에 담아주기.

df_column_concat = pd.concat([df4,df5,df6], axis=1, join='inner')#공통된 인덱스만 남기면 공통되지 않는 값은 빠진다.


#공통된 열을 기준으로 연결하기(marge)

df = pd.read_csv('data/scores.csv')
df7 = df.loc[[1,2,3]['name', 'eng']]
df8 = df.loc[[1,2,3]['name', 'math']]
#이름이라는 칼럼이 공통되기 때문에 네임 칼럼 안의 공통된 값만 출력 될것.

pd.merge(df7, df8, on = 'name')

#아우터 는 공통되지 않은 데이터를 삭제하지 않겠다. 반대로 이너는 공통되지 않는것들을 전부 삭제하겠다.콘캣은 아우터, 머지는 이너

pd.merge(df7, df8, on = 'name', how = 'outer')#이러면 공통되지 않은애들도 삭제되지 않음
pd.merge(df7, df8, on = 'name', how = 'left')#왼쪽 기준으로 모으기
pd.merge(df7, df8, on = 'name', how = 'right')#오른쪽 기준으로 모으기



