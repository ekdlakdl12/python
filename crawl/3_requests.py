import requests

res = requests.get("http://naver.com")

#print("응답코드:",res.status_code) #응답코드 200출력시 정상 나머진 오류


#오류 잡는 로직 ===> 이렇게 간단하게씀 res.raise_for_status() #오류날시 종료
#if res.status_code == requests.codes.ok:
#    print("정상입니다")
#else:
#    print("문제가 생김.[에러코드",res.status_code,"]")


print(len(res.text))
print(res.text)

# mygoogle html 파일 생성  utf8로 
with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)
    
    

