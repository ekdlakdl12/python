# 0~99 숫자 정수 입력
# 입력 숫자 10보다작으면 *10 해서 2자리로 만들기
# 그다음 주어진수 가장 오른쪽수랑 자리별로 더한수의 값의 오른쪽값


#0~99정수입력
n= input()
#if 길이 비교용
num = n
#count
cnt = 0

while True:
    #조건에 맞도록 초기값이 10미만이면 0추가
    if len(num) == 1:
        num = "0" + num
    #문자열을 int로 바꿔서 더함
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1]
    #count
    cnt = cnt + 1
    #초기값으로 돌아오면 cnt 출력후 종료
    if num == n:
        print(cnt)
        break

    

#답은 맞앗는대 메모리 초과해서 정답처리가 안됨 억울
