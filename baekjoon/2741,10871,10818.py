#백준 테스팅 파일입니다 현 프로젝트와는 관련이 없습니다

#2741
"""
n= int(input(''))
#for i in range(1,n+1):
#    print(i)
"""

#10871
"""
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
"""

#10818
"""
cnt = int(input()) #count
numbers = list(map(int, input().split())) #list에 숫자 입력
max = numbers[0] #max값
min = numbers[0] #min값

for i in numbers[1:]: #입력받은 numbers배열 1번째부터 : ~끝까지
    if i > max: #number[1]은 max 보다 큰가?
        max = i #크면 i에 대입
    elif i < min: #min이 더크면 min에 대입
        min = i

print(min,max) #출력
"""


