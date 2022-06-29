"""
https://www.acmicpc.net/problem/1600
말이 되고픈 원숭이 / 골드 5 / 2시간
실패 3(시간초과 2 , 틀렸습니다 1)

"""
import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W,H = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(H)]
horse_x = [2,2,1,1,-1,-1,-2,-2]
horse_y = [-1,1,-2,2,-2,2,-1,1]
X  = [-1,1,0,0]
Y  = [0,0,-1,1]
visited = [[0 for _ in range(W)] for _ in range(H)] # visited에 남은 말 점프 횟수
visited[0][0] = K+1 
# 말 횟수가 다 쓴 경우와 미방문을 구별하기 위하여 1~K+1로 표시(K+1의 경우 : K번의 말 점프 남음)


def is_visited(x,y,dx,dy,horses):
    nx,ny = x+dx, y+dy
    if 0<=nx<H and 0<=ny < W:
        if  G[nx][ny]== 0:
            # 현재 말 점프횟수가 해당칸의 말 점프횟수-1보다 큰 경우 업데이트후 큐에 추가
            if visited[nx][ny]-1 < horses:
                visited[nx][ny] = horses+1
                return True
    return False

def bfs():
    answer = -1
    Q = deque()
    Q.append([(0,0),K,0])

    while Q:
        (x,y),jump,cnt = Q.popleft()
        if x == H-1 and y == W-1: # 정답
            answer  = cnt
            break
        if jump>0:
            # 말을 이용한 방문
            for hx,hy in zip(horse_x,horse_y): 
                ans = is_visited(x,y,hx,hy,jump-1)
                if ans:
                    Q.append([(x+hx,y+hy),jump-1,cnt+1])
        for dx,dy in zip(X,Y):
            # 그냥 방문
            ans = is_visited(x,y,dx,dy,jump)
            if ans:
                Q.append([(x+dx,y+dy),jump,cnt+1])
    print(answer)
bfs()
