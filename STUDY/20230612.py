이메일 = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

from re import findall, match #파인드 올이나 매치 함수 사용할것이라 선언

for e in 이메일.split(sep='\n') :
    result = e.findall("a-z")
    e.group()
    'python'
    print(e)

