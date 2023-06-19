import pandas as pd
import numpy as np

#5.2.6 Function Application and Mapping
# pandas 객체에 Numpy 의 유니버설 함수(배열의 각 원소에 적용되는 메서드) 적용 가능
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
 index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
np.abs(frame)
# 자주 사용되는 또 다른 연산은 각 컬럼이나 로우의 1 차원 배열에 함수를 적용하는 것
# DataFrame 의 apply 메서드 사용
f = lambda x: x.max() - x.min() # 최대값 - 최소값
frame.apply(f)
# apply 함수에 axis = 'columns' 설정시 각 로우에 대해 한 번씩만 수행
frame.apply(f, axis='columns')
# 배열에 대한 일반적인 통계(예, sum, mean)는 DataFrame 의 메서드로 존재하므로 apply 메서드, 사용 불필요
def f(x):
 return pd.Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)
# 배열의 각 원소에 적용되는 파이썬의 함수 사용 가능
# frame 객체에서 실숫값을 문자열 포맷으로 변환하고 싶다면 applymap 메서드 사용
format = lambda x: '%.2f' % x
frame.applymap(format)
# Series 는 각 원소에 적용할 함수를 지정하기 위한 map 메서드를 가지고 있기 때문에
# 이 메서드 이름이 applymap
frame['e'].map(format)