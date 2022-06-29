# 위에서 아래로

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True) # 내림차순
print(*arr)
