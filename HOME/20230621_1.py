import pandas as pd

df = pd.read_csv('data/scorse.csv')
df = df.head()
df_copy = df.copy()


#특정 칼럼내의 데이터에 일정한 수를 더하기
df_copy.math = df.math+5
print(df_copy)#이러면 출력시 100점을 넘는 점수가 생기는데, 밑은 그걸 방지하기 위한 메소드다.

#일정 점수 이상 오버되는걸 막기 위한 메소드
def plus5(x):
    score = x+5
    if score >= 100:
        score = 100
    return score
df['math'].apply(plus5)#아직 출력만 한 상태, 저장은 아직 안함.

df_copy['math'] = df['math'].apply(plus5)#이렇게 해야 저장이 됨.
#클래스의 (x)는 df['math']의 메스 매개변수를 받는거라 따로 적어줄 필요가 없다.
print(df_copy)


#상한(100)이 정해져 있으면서, 매개변수(n)로 그때그때 원하는 점수가 추가되도록 하는 식.
def plusn(x,n):
    score = x+n
    if score >= 100:
        score = 100
    return score
df['eng'].apply(plusn, n=1)#역시 이렇게만 하면 출력만 가능, 저장은 안됨.
df_copy['eng'] = df['eng'].apply(plusn, n=1)#이렇게 담아줘야 변경사항저장 가능.



# 
# ##