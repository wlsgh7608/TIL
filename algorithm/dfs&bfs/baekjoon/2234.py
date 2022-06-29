"""
성곽 / 골드 4 / 30분
실패1 (틀렸습니다 1(출력문을 안뻈음))
"""
import sys
input = sys.stdin.readline
from collections import deque
def have_wall(n):
    results = []
    for _ in range(4):
        if n%2 == 1:
            results.append(True)
        else:
            results.append(False)
        n = n//2
    return results # 서북동남

N,M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
D = {0:(0,-1),1:(-1,0),2:(0,1),3:(1,0)}

room_cnt = 0
max_room = 0
wall_cut = 0

def bfs(x,y):
    Q = deque()
    visited[x][y] = True
    cnt = 0
    Q.append((x,y))
    while Q:
        cnt+=1
        x,y = Q.popleft()
        can_go = have_wall(G[x][y])
        for idx,wall in enumerate(can_go):
            if not wall:
                nx,ny = x+D[idx][0],y+D[idx][1]
                if 0<= nx <M and 0<=ny<N:
                    if not visited[nx][ny] :
                        visited[nx][ny] = True 
                        Q.append((nx,ny))
    return cnt


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            room_cnt+=1
            max_room = max(max_room,bfs(i,j))


for i in range(M):
    for j in range(N):
        visited = [[False for _ in range(N)] for _ in range(M)]
        walls = have_wall(G[i][j])
        for idx,wall in enumerate(walls):
            if wall:
                new_i,new_j = i+D[idx][0],j+D[idx][1]
                if 0<=new_i<M and 0<=new_j<N and wall and not visited[i][j]:
                    wall_cut = max(wall_cut,bfs(i,j)+bfs(new_i,new_j))
        
print(room_cnt)
print(max_room)
print(wall_cut)

"""
11 14 7 11 6
3 14 5 15 5
5 15 5 3 12
9 14 13 13 15
"""