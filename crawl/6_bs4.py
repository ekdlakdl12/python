import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

#가져온 html 을 lxml 파서를통해 Beautifulsoup객체로 만듦
soup = BeautifulSoup(res.text, "html.parser")#이곳에 정보가 다들어가잇음 #xml 안되서 html.parser 사용
#print(soup.title)
#print(soup.title.get_text()) #title에서 tag는빠지고 내용만출력됨
#print(soup.a.attrs) #attrs 속성값나옴
#print(soup.a["href"]) #처음반환되는 a속성정보가 나옴/ a엘리먼트의 href속성값정보 추출

#print(soup.find("a",attrs={"class":"Nbtn_upload"}))
#print(soup.find(attrs={"class":"Nbtn_upload"})) #오류나서 실행이안됨 pip설치햇는대 안됫다는거마냥 적힘

#print(soup.find("li",attrs={"class":"rank01"}))
#rank1 = soup.find("li",attrs={"class":"rank01"})
#print(rank1.a) #a붙힐시 태그값만나옴

#print(rank1.a.get_text())
#rank2= rank1.next_sibling.next_sibling #줄바꿈
#rank3 = rank2.next_sibling.next_sibling
#print(rank3.a.get_text())
#rank2 = rank3.previous_sibling.previous_sibling #next와 반대 전으로 돌아감
#print(rank2.a.get_text())

#print(rank1.parent) #부모로감

#rank2 = rank1.find_next_sibling("li") #li태그를 찿기 이러면 시블링 두번안써도됨
#print(rank2.a.get_text())

#rank3 = rank2.find_next_sibling("li")
#print(rank3.a.get_text())

#rank2 = rank3.find_previous_sibling("li")
#print(rank2.a.get_text())

#형제들을 모두 가져오는
#print(rank1.find_next_siblings("li"))
#text = rank1.find_next_siblings("li")
#print(text.a.get_text())

# "a" tag의 text 속성에 입력된값을 찿아주는
#webtoon = soup.find("a",text="독립일기 11화  밥공기 딜레마")
#print(webtoon)
