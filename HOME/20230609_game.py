import random
list=['5성','4성','3성']
소환횟수 = 0
choices = []
for i in range(1,100):
    for i in range(1,10):
        소환 = random.choices(list,weights=[1.000,3.000,40.000],k=10)
        choices.appeand(소환[0])
        소환횟수 += 1
        print(choices)
    if '5성' in choices:
        print('축 5성')
        break
    else:
        print('아직 안나옴')
    choices.clear()
print('10연차를 몇번해야했나? : ',소환횟수)
print('사용한 성정석 : ',format(소환횟수*30),"개")
print('투자해야 하는 금액 : ',format(소환횟수*1230)*30,"원")

