import pandas as pd


df = pd.read_csv('data/scores.csv')
df.head()

#학생 총 인원 구하기
len(df)

#학생들에게 번호 열 추가하기
df['no'] = range(1,len(df)+1)

df['sum'] = df['kor'] + df['eng'] + df['math']
print(df)#출력시 'sum'이라는 열(세로줄)이 추가된다

df['no'] = +df['no']+99 #이러면 백으로 시작되어서, 하나씩 커지는 열이 추가됨

#컬럼 삭제법(열,세로줄)
df = df.drop(columns=['no','sum'])#둘 중 아무거나 선택하면 됨
df.drop(columns=['no','sum'], inplace=True)#컬럼삭제하는법! inplace = 트루여야만 데이터베이스에 삭제가 저장된다. 
#컬럼스 대괄호 안에 삭제할 컬럼명 등록

#컬럼명변경하는 법
#컬럼명 한번에 바꾸는 법
df.columns=['이름','국어','영어','수학']#컬럼명 리스트와 전체 컬럼명 수가 다르면 에러
#입력한 순서대로, 컬럼명이 바뀐다.

#특정 컬럼명만 바꾸기
df.rename(columns = {'이름':'성명'}, inplace=True)
#inplace=True 가 되어야 저장된다.
#혹은 df = df.rename(columns={'이름':'성명'}, inplace=True) 하고 df에다가 한번 더 담아줘야 저장된다.
#딕셔너리 형태로 {현재 컬럼명 : 바꿀이름} 전달.
