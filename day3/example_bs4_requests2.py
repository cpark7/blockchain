import requests
from bs4 import BeautifulSoup

req = requests.get('https://land.naver.com/news/headline.nhn')
source = req.text
soup = BeautifulSoup(source,'html.parser')


top_list1 = soup.select("#content > div.section_headline.NE\=a\:mnn > ul > li > dl > dt:nth-child(2) > a")
top_list2 = soup.select("#content > div.section_headline.NE\=a\:mnn > ul > li > dl > dt:nth-child(1) > a")
# dt <<로 생겼으나 dtLnth-child(1) 로 바꾼거야 편하게하려고?ㅋㅋㅋㅋㅋㅋㅋ
top_list = list()

for t1 in top_list1:
    top_list.append(t1.string)

for t2 in top_list2:
    if t2.string == None:
        continue
    else:
        top_list.append(t2.string)
for top in top_list:
    print(top)
#content > div.section_headline.NE\=a\:mnn > ul > li:nth-child(2) > dl > dt:nth-child(2) > a
#content > div.section_headline.NE\=a\:mnn > ul > li > dl > dt:nth-child(2) > a
#content > div.section_headline.NE\=a\:mnn > ul > li:nth-child(1) > dl > dt > a
#content > div.section_headline.NE\=a\:mnn > ul > li > dl > dt > a



#main_content > div.list_body.newsflas//*[@id="main_content"]/div[2]/ul[1]/li[6]/dl/dt/ah_body > ul.type06_headline > li:nth-child(6) > dl > dt > a