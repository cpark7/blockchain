def calcstep(begin, end, step=1):
    sum = 0

    for num in range(begin,end+1,step):
        sum = sum + num
    return sum

print("1~10", calcstep(1,10,2))
print("1~100", calcstep(1,100))

# 함수 가변데이터 << *