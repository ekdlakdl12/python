#웹툰 가우스전자 크롤

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

#가져온 html 을 lxml 파서를통해 Beautifulsoup객체로 만듦
soup = BeautifulSoup(res.text, "html.parser")
#cartoons = soup.find_all("td",attrs={"class":"title"})
#title = cartoons[0].a.get_text()
#속성값은 a.[]
#link = cartoons[0].a["href"]
#print(title)
#print("https://comic.naver.com" + link)

#for cartoons in cartoons:
    #title = cartoons.a.get_text()
    #link = "https://comic.naver.com" + cartoons.a["href"]
    #print(title,link)

# 평점구하기

cartoons = soup.find_all("div",attrs={"class":"rating_type"})

total = 0

for cartoons in cartoons:
    rate = cartoons.find("strong").get_text()
    print(rate)
    total += float(rate)
    print("전체점수: ",total)
    print("평균점수: ",total / len(cartoons))


