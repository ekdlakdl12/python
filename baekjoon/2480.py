#랜덤 사용한방법 - 백준에 제출하면 오류남 조건이안맞음
import random


a =random.randint(1,6)
b =random.randint(1,6)
c =random.randint(1,6)

print(a,b,c)

#3개의 눈이 같은경우
if a == b == c:
     print(10000+(a*1000))
#2개의 눈이 같은경우
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)    
#하나도 같은숫자가 없을경우
else:
    print(max(a,b,c)*100)
     
     
#입력방법   
        

#a,b,c=map(int,input().split())
#if a==b==c:
    #print(10000+a*1000)
#elif a==b or b==c:
    #print(1000+b*100)
#elif a==c:
    #print(1000+a*100)
#else:
    #print(max(a,b,c)*100)
        
