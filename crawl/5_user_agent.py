import requests

url = "http://nadocoding.tistory.com"

#유저 Agent 정보
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
#headers안에 있는 값을 입력함으로써 html 소스가 재대로 나옴

res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

with open("nadocoding.html","w",encoding="utf8") as f: #주소 오픈하고 utf8로 파일만들어라
    f.write(res.text)
