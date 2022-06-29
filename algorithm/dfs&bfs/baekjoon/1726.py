"""
https://www.acmicpc.net/problem/1726
로봇 / 골드 3/ 70분
실패 2 (틀렸습니다 1 , 메모리 초과 1)
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [list(map(int,input().split()))for _ in range(N)]
P = {0:0,1:2,2:1,3:3} # 동서남북
D = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)} # 동남서북
start = list(map(int,input().split()))
end = list(map(int,input().split()))
start[0] -=1
start[1] -=1
start[2] = P[start[2]-1]
end[0] -=1
end[1] -=1
end[2] = P[end[2]-1]

def is_possible(x,y,d,cnt):
    if 0<=x<N and 0<=y<M:
        if not visited[x][y][d] and not G[x][y]:
            visited[x][y][d] = True
            Q.append((x,y,d,cnt+1))
            return True
        elif not G[x][y]:
            return True
    return False

visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
from collections import deque
Q = deque()
a,b,c = start
Q.append((a,b,c,0))
visited[start[0]][start[1]][start[2]] = True
cnt = 0
while Q:
    x,y,d,cnt = Q.popleft()
    if [x,y,d] == end:
        break

    for i in range(1,4):
        nx = x + i*D[d][0]
        ny = y + i*D[d][1]
        result = is_possible(nx,ny,d,cnt)
        if result == False:
            break
    nd = (d+1)%4
    if not visited[x][y][nd]:
        visited[x][y][nd] = cnt+1
        Q.append((x,y,nd,cnt+1))

    nd = (d-1)%4
    if not visited[x][y][nd]:
        visited[x][y][nd] = cnt+1
        Q.append((x,y,nd,cnt+1))
print(cnt)


"""
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
3 3 2
5 2 1


5 4
1 1 1 0
1 1 0 0
0 0 0 0
0 1 0 1
0 0 0 1
5 1 1
1 4 4

answer 6


"""