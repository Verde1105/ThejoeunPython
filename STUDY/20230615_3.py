import pandas as pd
df = pd.read_csv('data/scores.csv')
df.index= 'i'+df.index.astype('str')
df.head()

s1=df.loc['i3']
type(s1)
s1.index
s1.values


df.loc[['i1','i3','i5']] #인덱스가 해당되는 행 추출하기
df.loc[['i3']] #인덱스가 i3인 행을 데이터 프레임 형태로 추출하기. 인덱스에 없는 값을 사용하면 에러가 발생.

df.loc['i1','kor'] #인덱스 i1의(열) kor(행,칼럼) 점수를 출력하라. //교차점으로 조건만든듯
type(df.loc['i1','kor'])#타입 출력은 이런식으로



df.loc['i1',['name','kor']]#인덱스명 + 컬럼명 리스트
type(df.loc['i1',['name','kor']])

df.loc[['i1','i3','i5'],'name']#해당 인덱스의 이름을 가져와라
df.loc[['i1','i3','i5'],['name','kor']]

df.loc[:,'name']#모든 행에서 해당 칼럼 내용을 가져온다. 시리즈형태
df.loc[:,['name']]#모든 행에서 해당 칼럼 내용을 가져온다. 항목하나인 리스트형태 = 데이터프레임 형태로 가져올수있다.

df.loc[:,['name','math']]#한번에 두가지 이상의 칼럼안의 모든 내용 가져오기.



