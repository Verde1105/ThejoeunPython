import pandas as pd


# 문자열을 담고 있는 컬럼에 누락된 값이 포함된 경우
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
 'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(data)
data
data.isnull()
# 문자열과 정규 표현식 메서드는 data.map 을 사용하여 각 값에 적용(lambda 혹은 다른 함수 이용), ...할 수 있지만 NA 값을 만나면 실패함.
# 이런 문제를 해결하기 위해 Series 에는 NA 값을 건너뛰도록 하는 문자열 처리 메서드 'str.contains' 가 있음.
data.str.contains('gmail')
# 정규표현식을 IGNORECASE 같은 re 옵션을 함께 사용하는 것도 가능
# re.IGNORECASE : 대/소문자를 구분하지 않는 일치를 수행 (예, x = X)

#<<pattern>>
data.str.findall(pattern, flags=re.IGNORECASE)
# 벡터화된 요소를 꺼내 오는 방법: str.get 이용 또는 str 속성의 색인 이용
matches = data.str.match(pattern, flags=re.IGNORECASE)
matches
# 내재된 리스트의 원소에 접근하기 위해 색인 이용
matches.str.get(1) #지정된 위치 또는 키로 각 구성요소에서 요소를 추출.
# Index 1 에 해당하는 요소만 추출
matches.str[0]
data.str.get(1)
data.str[0]
# 문자열을 잘라내기
data.str[:5]


#<<백터화된 문자열 메소드>>

#cat : 선택딘 구분자와 함께 요소별로 문자열을 이어 붙인다.
#contains :  문자열이 패턴이나 정규 표현식을 포함하는지 나타내는 불리언 배열을 반환
#extract : 문자열에 담긴 Series 에서 하나 이상의 문자열을 추출하기 위해 정규표현식을 이용. 결과는 각 그룹이 하나의 컬럼이 되는 DataFrame
#endswith : 각 요소에 대해 x.endswith(pattern)과 동일한 동작을 한다.
#startswith : 각 요소에 대해 x.startswith(pattern)과 동일한 동작을 한다.
#findall : 각 문자열에 대해 일치하는 패턴/정규 표현식의 전체 목록을 구한다.
#get : i 번째 요소를 반환
#isalnum : 내장함수 str.isalnum 과 동일
#isalpha : 내장함수 str.isalpha 과 동일
#isdecimal : 내장함수 str.isdecimal 과 동일
#isdigit : 내장함수 str.isdigit 과 동일
#islower : 내장함수 str.islower 과 동일
#isnumeric : 내장함수 str.isnumeric 과 동일
#isupper : 내장함수 str.isupper 과 동일
#join : Series 의 각 요소를 주어진 구분자로 연결
#len : 각 문자열의 길이
#lower, upper : 대소문자로 변환
#match : 주어진 정규 표현식으로 각 요소에 대한 re.match 를 수행하여 일치하는 그룹을 리스트로 반환
#pad : 문자열의 좌우 또는 양쪽에 공백을 추가
#center : pad(side = 'both')와 동일
#repeat : 값을 복사 예)s.str.repeat(3)은 각 문자열에 대한 x*3 과 동일
#replace : 패턴/정규 표현식과 일치하는 내용을 다른 문자열로 치환
#slice : Series 안 에 있는 각 문자열을 자른다.
#split : 정규표현식 혹은 구분자로 문자열을 나눈다.
#strip : 왼쪽과 오른쪽의 공백 문자 제거
#rstrip : 오른쪽의 공백 문자 제거
#lstrip : 왼쪽의 공백 문자 제거





