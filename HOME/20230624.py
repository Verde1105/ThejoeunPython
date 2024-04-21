import numpy as np


#단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)


#복수 객체 저장 및 불러오기
array1 = np.array(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz', array1 = array1, array2 = array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)

#넘파이 원소 오름차순 정렬
array3 = np.array([5,9,10,3,1])
array.sort()
print(array)
#만약 거꾸로 내림차순으로 정렬하고 싶다면, print(array[::-1]) 로 설정하여 낮은것부터 출력되도록 하면 된다.

#각 열을 기준으로 정렬
array4 = np.array([[5,9,10,3,1],[8,3,4,2,5]])
print(array4)
array.sort(axis=0)
print(array4)

#<<이하 자주 써먹는 것>>
#균일한 간격으로 데이터 생성
array5 = np.linspace(0, 10, 5)#0~10 사이를 5개의 데이터가 채우도록 만드는 것.
print(array5)

#난수의 재현 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10 (2, 3)))#0~10까지의 숫자 중, 2열에, 각 숫자 3개로 고정

#넘파이 배열 객체 복사
#넘파이는 동일한 주소를 가르킨다면, 하나를 수정했을때 ,다른 동일 주소를 가진 것들 전부가 수정된다.
array6 = np.arange(0,10)
array7 = array6
array7[0] = 99
print(array6)
#위의 결과대로라면 어레이6을 손대지 않고, 어레이7을 수정할때, 어레이6까지 값 수정이 가능하다.

array6 = np.arange(0,10)
array7 = array6.copy()#이렇게 카피를 해줘야 다른 동일주소를 가진 어레이들이 바뀌지 않는다.
array7[0] = 99
print(array6)

#중복된 원소 제거
array8 = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array8))#중복 원소 제거, 하나씩만 출력.

