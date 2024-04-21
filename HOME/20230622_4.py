import pandas as pd


df = pd.read_csv('data/scorse.csv')
df.head(3)


#데이터 사용 전 먼저 결측치 확인하기
df.info()
#이러면 결측치가 있는지 나올것이고, 나온다면 전부 삭제할 예정.


df.dropna(inplace=True)#널값있는 행 삭제하고 저장
df.isnull().sum()#결측치 확인

#평균점수 계산하기
df['average'] = round((df.kor+df.eng+df.math)/3,1)#소수점이 너무 많아지니 round로 보여지는 소숫점 자리를 정리.
#라운드를 사용하여 계산한 평균값을 에버리지 컬럼을 만들어 넣기.
df.head(1)


def get_grade(x):
    if x >= 90:
        return 1
    elif x >= 80:
        return 2
    elif x >= 70:
        return 3
    elif x >= 60:
        return 4
    else:
        return 5
    
df['average'].apply(get_grade)#에버리지 칼럼에, 등급 메소드를 적용하겠다.
df['grade'] = df['average'].apply(get_grade)#그레이드 칼럼을 만들어 안에, 에버리지 칼럼에, 등급 메소드를 적용한것을 담겠다.

df.dtypes#각 칼럼의 자료형 확인하기

df['grade'] = df['grade'].astype('category') #반드시 담아야지만 저장이 된다.

df['grade'].dtype#카테고리 타입 확인

df['grade'].cat.categories = ['A','B','C','D']#카테고리 이름 바꾸기. 이러면 숫자가 대괄호 안의 영어로 바뀐다.

#누락된 카테고리 추가
df['grade'] = df['grade'].cat.set_categories(['A','B','C','D','F'])#반드시 받아두기. 누락된 'f' 추가
df['grade'].dtype


df_titanic = pd.read_csv('data/titanic.csv')
df_titanic.head(1)

#내용물 확인
df_titanic['Pclass'].unique()
df_titanic['Sex'].unique()
df_titanic['Embarked'].unique()

#용량 확인하기
df_titanic.info()


#카테고리 자료형으로 바꾸기
df_titanic['Survied'] = df_titanic['Survied'].astype('category')
df_titanic['Pclass'] = df_titanic['Pclass'].astype('category')
df_titanic['Sex'] = df_titanic['Sex'].astype('category')
df_titanic['Embarked'] = df_titanic['Embarked'].astype('category')

#데이터 타입 카테고리형으로 잘 바뀌었는지 확인
df_titanic.dtypes

#용량확인
df_titanic.info()#카테고리형을 바꾸면 메모리 사용량이 많이 줄어든다



