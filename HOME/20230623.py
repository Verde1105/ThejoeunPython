import pandas as pd

df = pd.read_csv('data/birth_die.csv')

#시계열 데이터


df.dtypes
#각 칼럼이 어떤 타입인지


#출생, 사망 컬럼을 데이트 타임 자료형으로 변환
pd.to_datetime(df['출생'])
#아직 여기까지만 하면 저장이 안됨

df['출생'] = pd.to_datetime(df['출생'])
df['사망'] = pd.to_datetime(df['사망'])


#출생 컬럼 0번 인덱스의 연도
df['출생'][0].year

#출생 컬럼의 연도
df['출생'].dt.year#연도만 가져오겠다
df['출생'].dt.month#월만 가져오겠다
df['출생'].dt.day#일만 가져오겠다.

#분기 컬럼 만들기
df['출생'] = df['출생'].dt.quarter#몇분기인지 보여준다.


#시작날과 끝날이 있을때 생존일수 계산도 가능.
#생존일수 컬럼 만들어 데이터 담기
df['생존일수'] = df['사망'] - df['출생']

#생존 기간 컬럼 만들어 데이터 담기
df['사망'] = df['사망'].dt.year - df['출생'].dt.year

#요일, 월이름 추출하기
df['출생'].dt.strftime('%b')

#출생요일 컬럼
df['출생요일'] = df['출생'].dt.strftime('%a')

#출생월 컬럼 추가하기
df['출생월'] = df['출생'].dt.strftime('%b')


#데이트 타임 자료형을 인덱스로 만들어 사용하기
df.index = df['출생']

#1995년 출생한 데이터 추출하기
df.loc['1995']

#1995 년 2월 출생 데이터 추출
df.loc['1995-02']
