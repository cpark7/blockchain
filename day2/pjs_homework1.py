import random
dic = {1:"가위",2:"바위",3:"보"}
com = random.randrange(1,4)
while 1:
    user = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요:"))
    if user > 3 or user < 1:
        print("다시 입력하세요")
    else:
        break

print("COM : ",dic[com])
print("USER :", dic[user])
if com == user :
    print("비겼습니다.")
elif user - com == 1 or user - com < -1:
    print("이겼습니다.")
else:
    print("패배했습니다.")