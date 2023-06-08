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
a =[i for i in star if i +"\n" ]
print(a*10)
