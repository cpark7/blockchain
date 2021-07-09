import requests
from bs4 import BeautifulSoup

req = requests.get('https://finance.naver.com/news/')
source = req.text
soup = BeautifulSoup(source, 'html.parser')
#이쁘게 파싱된친구 출력하기
#print(soup.prettify())


#제목만 출력하기
"""
for i in range(6):
    print(soup.select("#newsMainTop > div > div.inner_area_left > div > div.main_news > ul > li > a")[i].string)
"""
#제목따오기
tmp = soup.select("#newsMainTop > div > div.inner_area_left > div > div.main_news > ul > li > a")

#print(tmp)
#for title in tmp:
#    print(title.string)

# 출처 따오기
company = soup.select("#newsMainTop > div > div.inner_area_left > div > div.main_news > ul > li > em")

for i in range(len(company)):
    print("{}[{}]".format(tmp[i].string,company[i].string))
