import sys

n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
# 벌 사이에 통이 있을떄
result1 = sum(li[1:n-1]) + max(li[1:n-1])
# 벌 전부 오른쪽에 통이 있을떄
result2 = 0
for i in range(1, n-1):
    a = sum(li[1:n]) - li[i] +sum(li[i+1:n])
    if a > result2:
        result2 = a

result3 = 0
for i in range(n-2, -1, -1):
    b= sum(li[0:n-1]) - li[i] + sum(li[0:i])

    if b > result3:
        result3 = b

print(max(result1, result2, result3))

