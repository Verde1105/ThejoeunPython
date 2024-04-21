import pandas as pd

#피봇테이블로 데이터 집계하기

df = pd.DataFrame({"item" : ["셔츠","셔츠","셔츠","셔츠","셔츠","바지","바지","바지","바지",],
                   "color": ["휜","휜","검","검"]
                   "size" : ["s","l","l","s","s","l","s","s","l"],
                   "sale" : [1, 2, 2, 3, 3, 3, 4, 5, 6, 7],
                   "inventory" : [2, 4, 5, 5, 6, 6, 8, 9, 9]})

df
df.pivot_table(index='item', columns='size', values='inventory', aggfunc='sum')
#데이터를 집계해서 표로 나타내줌
#아이템, 사이즈 별 재고 합계

df.pivot_table(index=['item','color'], columns='size', values='inventory', aggfunc='sum')
#이중인덱스 생성.

df.pivot_table(index=['item','color'], columns='size', values='inventory', aggfunc='sum', fill_value= 0 )
#fill_value= 0을 넣어주면 널값은 자동으로 날려준다.

df.pivot_table(index=['item','color'], columns='size', values=['sale','inventory'], aggfunc='sum', fill_value= 0 )
#이중인덱스 + values를 리스트로 줘서, 최고위 칼럼으로 보이는것이 생성되었다.


#타이타닉 객실등급에 따른 생존자 집계 구해보기
df = pd.read_csv('data/titanic.csv')
df_titanic = df[['survivend', 'pclass','sex','age','embarked']]
df_titanic = df_titanic.dropna()
df_titanic.head()

len(df_titanic)

df_titanic.pivot_table(index='sex',columns='pclass',values='survivend',aggfunc='count', margins=True )
#margins=True 를 넣어주면 전체 합계도 볼수가 있다.
#총 승선자 수 구하는 식

df_titanic.pivot_table(index='sex',columns='pclass',values='survivend',aggfunc='mean', margins=True )
#생존자 평균 구하기
#aggfunc='mean' <<푱균값구하는법. 다만, 디폴트가 평균값 구하기라 통채로 빼버려도 결과는 똑같이 평균값을 계산해준다.




