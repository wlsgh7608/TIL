"""
단지번호 붙이기
https://www.acmicpc.net/problem/2667
15:37 ~ 15:54
G[x][y] 값이 1일 경우 dfs 시작하고 단지 내 아파트 값을 리스트에 추가
인접한 아파트(상,하,좌,우) 체크
방문한 아프트 값 2
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    cnt = 1
    if 0<=x<N and 0<=y<N and G[x][y] == 1: # 방문하지 않았다면
        G[x][y] = 2 # 방문 표시
        cnt+=dfs(x-1,y)
        cnt+=dfs(x,y-1)
        cnt+=dfs(x,y+1)
        cnt+=dfs(x+1,y)
        return cnt
    return 0


N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int,input())))

apts = []

for i in range(N):
    for j in range(N):
        if G[i][j]==1:
            apts.append(dfs(i,j))
apts.sort() # 단지 내 아파트 수 오름차순 정렬
print(len(apts)) # 단지 수 
for apt in apts:
    print(apt)