"""
https://www.acmicpc.net/problem/14503

체크리스트
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
    - 현재 위치에서 4방향 체크 후 이동
"""
N,M = map(int,input().split())
x,y,d = map(int,input().split())

G = []
for _ in range(N):
    G.append(list(map(int,input().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
D = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
cnt = 0
fault = 0
while True:
    visited[x][y] = True
    ini_d = d
    for i in range(d-1,d-5,-1):
        cur_d = i%4
        nx = x + D[cur_d][0]
        ny = y + D[cur_d][1]
        if not visited[nx][ny] and not G[nx][ny] : # 위치,방향 할당
            x = nx
            y = ny
            d = cur_d 
            break
    else :
        # 4방향 모두 확인 후 이동하지 못하는 경우
        tmp = (ini_d+2)%4
        nx = x+ D[tmp][0]
        ny = y + D[tmp][1]

        if G[nx][ny]: # 1에 도착
            break
        else: # 한 칸 후진
            x = nx
            y = ny
ans  = 0
for raw in visited:
    ans +=sum(raw)
print(ans)