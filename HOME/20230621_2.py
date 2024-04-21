import pandas as pd

df = pd.read_csv('data/scorse.csv')
df = df.head()
df.index = df.Name
df.drop(columns=['Name'], inplace = True)
df_copy = df.copy()

#행(가로)단위 데이터 출력
def print_me(x):
    print(x)
df.apply(print_me, axis=1)

#합계구하기
def get_sum(x):
    return x.sum()

#학생별 점수 구하기
df_copy['sum' ]= df.apply(get_sum, axis=1)

#과목별 점수 합계
df.apply(get_sum, axis=0)#이것만으론 부족
df_copy.loc['sum'] = df.apply(get_sum, axis=0)#저장까지 하게 되었다.


