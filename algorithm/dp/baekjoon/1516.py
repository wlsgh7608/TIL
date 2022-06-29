"""
https://www.acmicpc.net/problem/1516
게임 개발 / 골드 3 / 
16:15 ~ 
"""
from collections import deque
N = int(input())
Q = deque()
cnt_box = [0 for _ in range(N)]
result = [0 for _ in range(N)]
building = [0 for _ in range(N)]
G =[[] for _ in range(N)]
befores = [[] for _ in range(N)]
for i in range(N):
    a,*b = map(int,input().split())
    building[i] = a
    for j in b:
        if j==-1:
            break
        cnt_box[i]+=1
        G[j-1].append(i)
        befores[i].append(j-1)

times = 0
for i in range(N):
    if cnt_box[i] == 0:
        result[i] = building[i]
        Q.append(i)

while Q:
    current = Q.popleft()
    for next in G[current]:
        cnt_box[next] -=1
        if cnt_box[next]==0:
            max_times = 0
            for p in befores[next]:
                max_times = max(max_times,result[p])
            ans = max_times+building[next]
            result[next] = ans
            Q.append(next)
for res in result:
    print(res)