for i in range(5):
    print(str(i)+ "=반복변수")
print()

li = [1,22,333,4444,55555]

for element in li:
    print(element)

for ele in range(len(li)):
    print("{}번째 반복: {}".format(ele,li[ele]))


#n_list = [x * 3 for x in li if x >= 1]

star = "*"
#a =[i for i in star if i +"\n" ]
for a in star:
    print(a*2)
    for b in star:
        print(b)

size = 5  # 별의 크기 설정

for i in range(size):
    for j in range(i + 1):
        print("*", end=" ")
    print()

size = 5  # 별의 크기 설정

for i in range(size):
    print(" " * (size - i - 1), end="")
    print("*" * (2 * i + 1))

size = 5  # 별의 크기 설정

for _ in range(size):
    stars = ["*"] * size  # 별로 이루어진 리스트 생성
    print(" ".join(stars))
