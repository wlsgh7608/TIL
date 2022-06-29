"""
https://www.acmicpc.net/problem/10971
외판원 순회 2 / 실버 2 / 29분
16:23 ~ 16:49
21:48 ~ 21:54
"""
import sys
input = sys.stdin.readline
N = int(input())
cities = list(range(N))
G = []
for _ in range(N):
    row = list(map(int,input().split()))
    G.append(row)

visited  = [False for _ in range(N)]
visited[0] = True
# dfs 로 순열 구현하기
per = []
def dfs(level,c_list):
    if level == N:
        per.append(c_list[:])
        return
    
    for i,val in enumerate(cities):
        if visited[i]:
            continue
        c_list.append(val)
        visited[i] = True
        dfs(level+1,c_list)
        c_list.pop()
        visited[i] = False

dfs(1,[0])
min_dist = sys.maxsize
for p in per:
    is_zero = False
    dist = 0
    for i in range(N):
        current = p[i]
        next = p[(i+1)%N]
        if not G[current][next]:
            is_zero = True 
        dist += G[current][next]
    # 갈 수 없는 경우(G값이0) 다음 반복문 실행
    if is_zero:
        continue
    min_dist = min(min_dist,dist)
print(min_dist)


"""
4
0 0 10 10
10 0 3 10
10 10 0 3
3 10 10 0
"""