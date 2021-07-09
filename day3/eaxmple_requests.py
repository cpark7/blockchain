import requests
URL = 'http://www.naver.com/'
response = requests.get(URL)
print(response.text)