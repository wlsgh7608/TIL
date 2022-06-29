# 게임 개발
"""
- [ ] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 현재 상황에서 4방향을 모두 체크한다.
  - 만약 4방향 모두 갈 수 없을 시 현재 방향에서 뒤로 간다. (이 떄 바다이거나 맵의 끝인지 판별)
시간복잡도 : O(1)

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
        if not visited[nx][ny] and not G[nx][ny] :
            x = nx
            y = ny
            d = cur_d 
            break
    else :
        tmp = (ini_d+2)%4
        nx = x+ D[tmp][0]
        ny = y + D[tmp][1]

        if G[nx][ny]:
            break
        else:
            x = nx
            y = ny
ans  = 0
for raw in visited:
    ans +=sum(raw)
print(ans)
"""
input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

output
3
"""