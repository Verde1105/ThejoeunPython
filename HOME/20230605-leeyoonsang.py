#문제 1 다음lst 변수를 대상으로 각 단계별로 list를 연산하시오

lst = [10, 1, 5, 2]

#단계1 :
step1 = lst * 2
print(step1)

#단계2 :

#첫번째 방법
step2 = lst * 2 + [20, ]
print(step2)

#두번째 방법
lst = [10,1,5,2]*2
lst[7] = 20
print(lst)
#세번째 방법
lst = [10, 1, 5, 2]
result = lst *2
double = lst[0]*2
result.append(double)
print(result)




#단계3:

result = step2[1::2]
print(result)


#문제2 A

size= int(input('vector의 수 : ' ))
lst = []
for i in range(size):
    lst.append(int(input()))
print('vector의 크기 : ', len(lst))

#문제2 B


    if int(input()) in lst:
        print('yes')
    else:
        print('no')


#문제 3

message = ['spam', 'ham','spam', 'ham','spam']
lst = [ 0 if i == 'spam' else 1 for i in message]
print(lst)


message = ['spam', 'ham','spam', 'ham','spam']
spam_list = [i for i in message if i  == 'spam']
print(spam_list)

#문제 4

position = ['과장', '부장', '대리', '사장', '대리', '과장']
no_duple = list(set (position))
print('중복되지 않은 직위 : ', no_duple)

frequency = {}
for d in position:
    frequency[d] = position.count(d)

print('각 직위별 빈도수 : ', frequency )

#다른 방법

from collections import Counter

position = ['과장', '부장', '대리', '사장', '대리', '과장']
print(Counter(position))


