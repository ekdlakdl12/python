N = int(input())
M = list(map(int, input().split()))
max_ = max(M)

for i in range(N):
    M[i] = M[i]/max_*100
print("%.2f" %(sum(M)/ N))