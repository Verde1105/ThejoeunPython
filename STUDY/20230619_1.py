import regex as re


# 이메일 주소를 검사하는 정규 표현식
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
# findall 메서드 사용 이메일 주소의 리스트 생성
regex.findall(text)
# search 는 텍스트에서 첫 번째 이메일 주소만 찾아준다.
# match 는 그 정규 표현 패턴이 문자열 내에서 위치하는 시작점과 끝점만을 알려준다.
m = regex.search(text)
m
text[m.start():m.end()]
# regex.match 는 None 반환. 왜냐하면 그 정규 표현 패턴이 문자열의 시작점에서부터 일치하는지 검사하기 때문
print(regex.match(text))
# sub 메서드는 찾은 패턴을 주어진 문자열로 치환하여 새로운 문자열 반환
print(regex.sub('REDACTED', text))
# 이메일 주소를 찾아서 사용자 이름, 도메인 이름, 도메인 접미사 로 나눠야 한다면 객 패턴을 괄호로 묶어준다.
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
# match 객체를 이용하면 groups 메서드로 각 패턴 컴포넌트의 튜플을 얻을 수 있다.
m = regex.match('wesm@bright.net')
m.groups()
# 패턴에 그룹이 존재한다면 findall 메서드는 튜플의 목록 반환
regex.findall(text)
# sub 역시 마찬가지로 \1, \2 같은 특수한 기호를 사용하여 각 패턴 그룹에 접근할 수 있다.
# \1 : 첫 번째로 찾은 그룹을 의미; \2 : 두번째로 찾은 그룹 의미
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))