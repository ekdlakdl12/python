p1 = [1,1,2,2,2,8]
p2 = list(map(int, input().split())) #공백으로 list 입력

print([p1i - p2i for p1i, p2i in zip(p1, p2)]) #리스트끼리 뺄셈