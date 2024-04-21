def show_price(shop):
    print(f'{shop}을 이용하려면')
    print('5천 골드 입니다.')
shop1 = '대장간'
show_price(shop1)
shop2 = '방앗간'
show_price(shop2)

def get_price(is_vip) :
    if is_vip == True :
        return 10000
    else :
        return 15000
    
def get_price(is_vip=False) :
    if is_vip == True :
        return 10000
    else :
        return 15000

def quest(today,*shops):#가변인자는 하나만 가능, 맨 끝에 위치
    print(today)
    for shop in shops:
        print(shop)
quest('2023년 6월 10일','옷가게')

quest('2023년 8월 15일','양털채집','대장간')

quest('2023년 8월 20일','옷가게','대장간','양털채집')


message='나는야 전역 변수.'
print(message)

def me():
    message='나는야 지역변수. 이름만 같은 동명이인 이라네.'
    print(message)
me()

def se():
    global message #message라는 이름의 전역 변수 사용하겠다, 선언. 없으면 이곳에서 제작.
    # message = '나는야 전역변수의 값을 제지정.'
    #이곳에 전역변수 값을 제지정하면, 선언된 전역변수값이 변경되어 출력. 지역변수로 바뀌는게 아님.

user_name = input('이름을 입력하시오.')
user_pw = int(input('패스워드를 입력하시오.'))
me1 = f'아이디는 공백을 넣을 수 없습니다. 다시 입력해주세요.'
me2 = f'입력하신 비밀번호를 확인해주세요. \n 입력하신 비밀번호 : {user_pw}'

if user_pw <= 0:
    print(me1)
    #user_pw() TypeError: 'int' object is not callable. 이러면 인트개체를 호출할수없다네, 왜지?
else :
    print(me2)


#새파일 만드는 법
f = open('list.txt','w',encoding='utf8') #('생성할파일이름.타입','언어','인코딩')
f.write('게임같은거 만들기 좋겠다.')
f.write('자바의 버퍼라이드인가? 꼭 그거같아.')
f.write('이걸로 뭘 더 할 수 있을까??')
f.close() #반드시 문단속!

#위에서 만든 새파일 읽는 법
f = open('list.txt','r',encoding='utf8') #('생성할파일이름.타입','사용할언어?','인코딩')
book = f.read() # f 전부 불러와
print(book) #책에 담아 보여줘.

for so in f:#for 문 사용하면 한줄씩 불러와서 so에 담아준다. 
    print(so,end='')#end 공백설정 하지않으면 빈 줄 하나 추가
f.close

#클로즈 안하는 자동법
with open('list.txt','r',encoding='utf8')as b2: #리스트를 b2에 담고
    book2 = b2.read() #책2에 b2=리스트 를 전부 담아줘.
    print(book2)#이제 책2 내용을 보여줘
    #위드를 쓰면 클로즈는 자동


