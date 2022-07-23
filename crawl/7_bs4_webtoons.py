#웹툰정보 다끌고오기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

#가져온 html 을 lxml 파서를통해 Beautifulsoup객체로 만듦
soup = BeautifulSoup(res.text, "html.parser")
# 속성이 a 이고 class값이 title인 모든 값을 가져오기
cartoons =soup.find_all("a",attrs={"class":"title"})
#alt shift f10 현재 코드 실행 단축키
#a element의 calss속성이 title인 모든 속성을 반환
for cartoons in cartoons: # for문에 넣으면 list
    print(cartoons.get_text()) #get text로 text만출력
