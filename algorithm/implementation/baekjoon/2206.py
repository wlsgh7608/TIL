"""
https://www.acmicpc.net/problem/2206
체크리스트
- [ ] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션,bfs 
- [✔] 알고리즘을 어떻게 구현하였는가?
    - 벽을 부술 수 있는 횟수는 1번임
    - 4방향에 대하여 벽인지, 길인지 체크
    - 벽을 뚫고 간 길에 대해서 뚫지 않고 가는 경우 체크
"""
from collections import deque
N, M = map(int,input().split())
G = []
for _ in range(N):
    row = list(map(int,input()))
    G.append(row)
visited = [[False for _ in range(M)] for _ in range(N)]
moves = [[-1,0],[1,0],[0,1],[0,-1]]

visited[0][0] = True
Q = deque()

cnt = 0
Q.append((0,0,1,1))
while Q:
    x,y,b,c = Q.popleft() #(x,y,can_break,count)
    if x == N-1 and y == M-1:
        print(c)
        break
    for move in moves:
        nx,ny = x+move[0],y+move[1]
        if nx>=0 and ny>=0 and nx<N and  ny<M:
            if not visited[nx][ny] and G[nx][ny]==0 : # 방문하지 않은 길이라면
                Q.append((nx,ny,b,c+1))
                visited[nx][ny] = True
            if b and G[nx][ny]==0 and visited[nx][ny]: # 벽을 뚫고 지나온 길을 뚫지 않고 갈 수 있다면
                G[nx][ny] =2
                Q.append((nx,ny,b,c+1))
                visited[nx][ny] = True
            if b and G[nx][ny]==1 : # 벽이라면 벽을 부숨(b=0)
                Q.append((nx,ny,0,c+1))
                visited[nx][ny] = True

if not visited[-1][-1]:
    print(-1)





""""
7 4
0000
1110
0000
0000
0111
0111
0010

"""