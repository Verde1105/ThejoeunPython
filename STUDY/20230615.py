import pandas as pd

# reindex: 새로운 색인에 맞도록 객체를 새로 생성
# 예제
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
# Series 객체에 대해 reindex 를 호출하면 데이터를 새로운 색인에 맞게 재배열하고,
# 존재하지 않는 색인 값이 있다면 NaN 을 추가한다.
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
#시계열 데이터를 재색인할 때 값을 보간하거나 채워 넣어야 할 경우 method 옵션을 이용하여 실행
# ffill 메서드를 이용하여 누락된 값을 직전의 값으로 채워 넣을 수 있다.
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
obj3.reindex(range(6), method='ffill')
# DataFrame 에 대한 reindex 는 로우(색인), 컬럼 또는 둘다 변경 가능
# 순서만 전달하면 로우가 재색인된다.
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
 index=['a', 'c', 'd'],
 columns=['Ohio', 'Texas', 'California'])
frame
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2
# 컬럼은 columns 예약어를 사용하여 재색인
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)
# 재색인은 loc 를 이용하여 라벨로 색인하면 좀 더 간결하게 할 수 있다.
frame.loc[['a', 'b', 'c', 'd'], states]