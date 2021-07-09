s = "짜장 짬뽕 탕수육"
print(s.split())

s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)

for c in city:
    print(c, "찍고",end = " ")

print()
s = "._."
print(s.join("대한민국"))

#fomat
price = 500
print("궁금하면 "+ str(price) + "원!")

print("궁금하면 %d원!" %price)
print("궁금하면 {}원!".format(price))

# 17page

month = 8
date = 15
anni = "광복절"
print("%d월 %d일은 %s이다"%(month,date,anni))