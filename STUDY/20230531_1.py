import math

print("=" * 5 , "문제4" , "=" * 5)

w1="word1"
w2="word2"
w3="word3"

abbr = w1[0]+w2[0]+w3[0]

print("첫번째단어 :" , w1)
print("두번째단어 :" , w2)
print("세번째단어 :" , w3)
print("=" * 10)
print("약자 : ",abbr)

print("=" * 5 , "문제3" , "=" * 5)



fat = input('지방의 무게를 입력하세요 : ')
carbohydrate = input('탄수화물의 무게를 입력하세요 : ')
protein = input('단백질의 무게를 입력하세요 : ')
di = int(fat) * 9 + int(protein) * 4 + int(carbohydrate) * 4
print('총칼로리 : ', format(di,"3,d"), 'cal')


print("=" * 5 , "문제2" , "=" * 5)



x = 2
y_1 = 2.5 * x**2 + 3.3 * x + 6
y_2 = 2.5 * math.pow(x,2) + 3.3 * x + 6
print(y_1)

print("=" * 5 , "문제1" , "=" * 5)

su = 5
dan = 800
print('su주소 : ',id(su))
print('dan주소 :',id(dan))
m = su * dan
print('금액 =',m)
