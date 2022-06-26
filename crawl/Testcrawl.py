from urllib.request import urlopen 
from bs4 import BeautifulSoup
import requests


url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() #오류날시 종료
soup = BeautifulSoup(res.text,"lxml")

#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #soup객체에서 처음 발견되는 a element 출력함
#print(soup.a.attrs)# a element의 속성정보를 출력함
#print(soup.a["href"]) #a element의 href속성 '값' 정보를 출력
#print(soup.find("a",attrs={"class:"Nbtn_upload})) #class="Nbtn_upload"인 a element를 찿기
#print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element를 찿아줘
#print(soup.find("li",attrs={"class":"rank01"}))
 
rank1 = soup.find("li",attrs={"class":"rank01"})
 
print(rank1.a)

      
      
