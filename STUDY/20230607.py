캐릭터 = {
    "이름" : "기사",
    "레벨" : 12,
    "아이템" : {
        "무기" : "불꽃의 검",
        "갑옷" : "풀 플레이트 아머"
    },
    "스킬" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in 캐릭터:
    if key == "아이템":
        for subkey in 캐릭터["아이템"]:
            # print("무기",":",캐릭터["아이템"]["무기"])
            print(subkey,":",캐릭터["아이템"][subkey])
    elif key == "스킬":
        for subkey in 캐릭터["스킬"]:
            print(key,":",subkey)
    else :
        print(key,":",캐릭터[key])
        

# for key in 캐릭터:
#     print(key,":",캐릭터[key])
# if "무기" in 캐릭터["아이템"]:
#     print("무기 : ")
# else:
#     print("프린트 잘못됨")
# for 스킬 in 캐릭터["스킬"]:
#     print("스킬 : ",캐릭터["스킬"])

    #n_list = [x * 3 for x in li if x >= 1]
    #for 아이템 in key:
    #    print(아이템,":",key)

