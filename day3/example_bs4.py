# 오늘은 크롤링해본대 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

from bs4 import BeautifulSoup

html_doc = '''<!doctype html>
<html lang="ko" data-dark="false"> 
<head> 
    <meta charset="utf-8"> 
    <title>NAVER</title> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
    <meta name="viewport" content="width=1190"> 
</head> 
<body> 
    <div id="u_skip"> 
        <a href="#newsstand"><span>뉴스스탠드 바로가기</span></a> 
        <a href="#themecast"><span>주제별캐스트 바로가기</span></a> 
        <a href="#timesquare"><span>타임스퀘어 바로가기</span></a> 
        <a href="#shopcast"><span>쇼핑캐스트 바로가기</span></a> 
        <a href="#account"><span>로그인 바로가기</span></a> 
    </div>
</body> 
</html>

'''

soup = BeautifulSoup(html_doc,'html.parser')

# html 전문 파싱 이쁘게 해둠.
#print(soup.prettify())
#제목만 가져오기
print(soup.title.string)
print(soup.find_all('a')[0])
print(soup.find_all('a')[0].string)

