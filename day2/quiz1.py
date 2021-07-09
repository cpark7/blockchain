import random

com = random.randrange(1,100)
check = 0
for i in range(1,6):
    print(i,"번째 시도:")
    user = int(input("컴퓨터의 숫자를 예상해보세요"))
    if com > user :
        print("너무 작아요")
    elif com < user:
        print("너무 커요")
    else:
        check = 1
        print("정답입니다.")
        print("당신은 {}번 만에 맞췄습니다.".format(i))
        break
if not check:
    print("당신은 5번 모두 틀렸습니다.")
