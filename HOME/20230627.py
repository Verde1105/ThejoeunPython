import pandas as pd

#열과 행의 형태 변경하기

df = pd.read_csv('data/scores.csv')
df = df.head(2)

df.melt()#그냥 멜트를 사용할시, 컬럼이 행으로 들어오게 될것이다.

#특정 행만 멜트시키지 않는 법.
df.melt(id_vars='name')#이러면 네임 행만 멜트되지 않음

#특정 행 하나가 아닌 두개 이상을 멜트시키고 싶지 않을 때.
df.melt(id_vars=['name','kor'])#칼럼명을 리스트 형태로 전달하면 두개 이상 가능

#특정 칼럼만 멜트시키고(행으로 내리고) 싶을떄
df.melt(id_vars='name', value_vars='kor')#이러면 네임은 고정되어있지만 국어는 행으로 내려오게 된다.

#특정 칼럼 두개를 행으로 내리고(멜트) 싶을때
df.melt(id_vars='name', value_vars=['kor', 'eng'])#이렇게 리시트로 전달하면 네임은 고정되어 있지만, 국어랑 영어가 행으로 내려온다.


#컬럼명 변경하기
df.melt(id_vars='name', value_vars=['kor', 'eng'], var_name='subject', value_name='score')
#이러면 value_name에 지정해준 값으로 칼럼명을 바꿀 수 있다.


#피봇pivot = 행으로 되어잇는것을 다시 열로 보내는것을 피봇이라 부른다.
df = pd.read_csv('data/scores.csv')
df = df.head(2)
df.melt(id_vars='name', value_vars=['kor', 'eng'], var_name='subject', value_name='score')

def get_grade(x):
    if x >= 90: grade = 'A'
    elif x >= 80: grade = 'B'
    elif x >= 70: grade = 'C'
    elif x >= 80: grade = 'D'
    else : grade = 'F'
    return grade

df['grade'] = df['score'].apply(get_grade)
df = df.sort_values('name')
df

#열을 행으로 보내기
df.pivot(index='name', columns='subject', values='score')# 이러면 인덱스(숫자)가 네임(글자)로 바뀐다.
#subject 칼럼에 있던, 국어, 영어, 수학이 전부 칼럼으로 올라온다.
#남는것은 점수밖에 없으니, 행에 남는것은, 점수 뿐.

df.pivot(index= 'name', columns= 'subject', values= 'grade')
#이번엔 남는것이 grade 등급밖에 없으니, 행에 남은것은 전부 등급 뿐.

#스코어와 등급 둘 다 동시에 넣고 싶다면
df.pivot(index= 'name', columns= 'subject', values= ['grade','score'])
#리스트 형태로 넣어주면 되고, 이러면 subject 처럼 최상위 칼럼과 같은 위치에 오게 된다.

#values(값)을 전달하지 않고도 위와 같은 출력이 가능하다.
df.pivot(index= 'name', columns= 'subject')


#행과 열을 서로 바꾸기
df.head
df.transpose()#행과 열이 서로 바뀜




