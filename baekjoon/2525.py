#오븐시계

H, M = map(int, input().split()) # 시간과 분을 입력받음
timer = int(input())  # 타이머 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)