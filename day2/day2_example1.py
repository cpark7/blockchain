#파이썬 기초 수업이라고 합니다.
## 1번 예제..

student = 1

while student <= 5:
    print(student, "번 학생의 성적을 처리한다. ")
    #student +=1
    student = student+1

for student in [1,2,3,4,5]:
    print(student, "번 학생의 성저글 처리한다. ")


num = 1
sum = 0

while sum <= 10:
    sum += num
    num +=1

print(sum)
print("test" , end = "")# printf <<not /n
print()
#1~100까지 짝수 홀수 합 따로 구하시오
odd = 0
even = 0

for i in range(1,101):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i

print("even", even)
print("odd", odd)