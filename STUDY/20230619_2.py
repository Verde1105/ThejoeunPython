import numpy as np
import pandas as pd
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)


# 계층적 색인에서 계층의 순서를 바꾸거나 지정된 계층에 따라 데이터를 정렬해야 하는 경우
# swaplevel 은 넘겨받은 두 개의 계층 번호나 이름이 뒤바뀐 새로운 객체를 반환(데이터는 불변)
#frame.swaplevel('key1', 'key2')
# sort_index 메서드는 단일 계층에 속한 데이터 정렬
# swaplevel 을 이용하여 계층을 바꿀 때
# sort_index 를 사용하여 결과가 사전적으로 정렬 가능
#frame.sort_index(level=1) # key2 기준 정렬
#frame.swaplevel(0, 1).sort_index(level=0)
# * 객체가 계층적 색인으로 상위 계층부터 사전식으로 정렬되어 있다면(sort_index(level=0)이나
# sort_index()의 결과처럼) 데이터를 선택하는 성능이 훨씬 좋아진다.

#8.1.2 Summary Statistics by Level
# DataFrame 과 Series 의 많은 기술 통계 및 요약 통계는 level 옵션을 가지고 있는데
# 한 축에 대해 합을 구하고 싶은 단계를 지정할 수 있는 옵션
#frame.sum(level='key2')
#frame.sum(level='color', axis=1)

#8.1.3 Indexing with a DataFrame's columns
# DataFrame 에서 로우를 선택하기 위한 색인으로 하나 이상의 컬럼을 사용하거나
# 로우의 색인을 DataFrame 의 컬럼으로 옮기고 싶은 경우
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
 'c': ['one', 'one', 'one', 'two', 'two',
 'two', 'two'],
 'd': [0, 1, 2, 0, 1, 2, 3]})
frame
# DataFrame 의 set_index()함수는 하나 이상의 컬럼을 색인으로 하는 새로운 DataFrame 을 생성
frame2 = frame.set_index(['c', 'd'])
frame2
