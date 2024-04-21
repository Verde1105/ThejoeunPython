#문1
lst = [10,1,5,2]
result = lst * 2
print('step1=',result)
result.append(lst[0]*2)
print('step2=',result)
result2 = []
for i in range(1, len(result),2):
    result2.append(result[i])
print('step3',result2)

#문2 A
vector = []
size = int(input('vector 수 :'))
for i in range(0,size):
    vector.append(int(input()))
print(f'vector의 크기: {len(vector)}')

#문2 B
vector = []
size = int(input('vector 수:'))
for i in range(0,size):
    vector.append(int(input()))
selectedValue = int(input())
isTrue = False
for i in vector:
    if i == selectedValue:
        isTrue = True
        break
if isTrue:
    print("YES")
else:
    print("NO")

#문제3
message = ['spam','ham','spam','ham','spam']
dummy = [1 if s.__eq__('spam') else 0 for s in message]
print(dummy)
spam_list = [s for s in message if s =='spam']
print(spam_list)

#문제4
position = ['과장','부장','대리','사장','대리','과장']
distinctPosition = set(position)
countPosition = {}
for key in position:
    countPosition[key] = countPosition.get(key,0)+1
print(f'중복되지 않은 직위: {list(distinctPosition)}')
print(f'각 직위별 빈도수: {countPosition}')

