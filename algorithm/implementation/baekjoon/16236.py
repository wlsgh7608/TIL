"""
https://www.acmicpc.net/problem/16236
아기상어 / 골드 3 / 180분
실패 2(시간 초과 2)

길찾기 - bfs
먹이발견 -> 길이 측정 -> 해당 길이 이하의 먹이 가져옴 -> 이후 먹이들 sort후 첫번째로 이동
-> 반복

"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
X = [-1,1,0,0]
Y = [0,0,-1,1]
Q = deque()
for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            fish_x = i
            fish_y = j
            Q.append((i,j,0))
visited = [[False for _ in range(N)] for _ in range(N)]
fish_size = 2
fish_cnt = 0

result = 0

feed_yet = True
feed_dist = sys.maxsize
feed_list = []
while Q:
    x,y,t = Q.popleft()
    # if t == feed_dist:
    #     break

    for dx,dy in zip(X,Y):
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<N :
            if not visited[nx][ny] and G[nx][ny]<=fish_size:
                visited[nx][ny] = True
                if 0<G[nx][ny]<fish_size:
                    feed_yet = False
                    feed_list.append((nx,ny,t+1))
                if feed_yet:
                    Q.append((nx,ny,t+1))
                    
    if not Q:
        if feed_list:
            feed_list.sort(key= lambda x:(-x[2],-x[0],-x[1])) # 길이,i,j순으로 sort
            fx,fy,ft = feed_list[-1]
            fish_cnt+=1
            result+=ft
            if fish_size == fish_cnt:
                fish_cnt=0
                fish_size+=1
            # 그래프 update
            G[fish_x][fish_y] = 0
            G[fx][fy]=9
            fish_x,fish_y = fx,fy
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[fx][fy] =True
            Q.append((fx,fy,0))
            feed_yet = True
            feed_list = []
            feed_dist = sys.maxsize
                
print(result)

