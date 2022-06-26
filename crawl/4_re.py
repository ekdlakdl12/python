#정규식1,2 - 전문가도 조금 어렵

# 정규식 라이브러리
import re

#abcd , book ,desk
#ca?e  = care , case ,cave
#caaae, cabe ,cace ,cade

p = re.compile("ca.e") 

# . (ca.e): care,cafe,case 하나의 문자를 의미함
# ^:(^de): desk,destination 문자열의 시작
# $ (se$) :case base(0) | face(x) 문자열의끝


def print_match(m):
    if m:
        print("m_group():",m.group()) #일치하는문자열반환
        print("m_string",m.string) #입력받은 문자열 출력
        print("m_start()",m.start()) #입력받은 문자열의 시작 index
        print("m_end()",m.end()) #입력받은 문자열의 끝 index
        print("m.span()",m.span()) #입력받은 문자열의 시작과 끝 index
    else:
        print("노매칭")


#m = p.match("good care") #match p에 들어가있는 ca.e 와 매칭이되는가
                    #print(m.group()) #매치되지않으면 에러가 발생
#print_match(m)


#m = p.search("good care") #주어진 문자열중에 일치하는게 존재하는지
#print_match(m)

lst = p.findall("cafe care") # 일치하는 모든것을 리스트 형태로 반환함
print(lst)





#정규식 순서 최종 정리

#1. p = re.compile("원하는 형태") / ca.e 등등 단어
#2. m = p.match("비교할 문자열") / good care 등등 : *처음부터* 일치하는지 확인
#3. m = p.search("비교할 문자열") :주어진 문자열중에 일치하는게 존재하는지
#4. lst = p.findall("비교할 문자열") # 일치하는 모든것을 리스트 형태로 반환함


#원하는 형태 : 정규식

# . (ca.e): care,cafe,case 하나의 문자를 의미함
# ^:(^de): desk,destination 문자열의 시작
# $ (se$) :case base(0) | face(x) 문자열의끝