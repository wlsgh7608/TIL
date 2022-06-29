"""
https://www.acmicpc.net/problem/17144
미세먼지 안녕! / 골드 4 / 70분 
실패3(시간초과 3)

"""
import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
G = [list(map(int,input().split()))for _ in range(R)]


X = [-1,1,0,0]
Y = [0,0,-1,1]
clock_D = [(0,1),(-1,0),(0,-1),(1,0)]
biclock_D = [(0,1),(1,0),(0,-1),(-1,0)]
airs = []
for i in range(R):
    for j in range(C):
        if G[i][j] == -1:
            airs.append((i,j))


def wind_num(x,y,num,new_G):
    for dx,dy in zip(X,Y):
        nx,ny= x+dx,y+dy
        if 0<=nx<R and 0<=ny<C and G[nx][ny]!=-1:
            new_G[nx][ny] += num 
            new_G[x][y] -= num

def expand(G):
    new_G = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if G[i][j]>=5:
                dusts = G[i][j]//5
                wind_num(i,j,dusts,new_G)
    G = [[G[i][j]+new_G[i][j] for j in range(C) ] for i in range(R)]
    return G

def air(x,y,direct):
    if direct==0: 
        D = clock_D
    else:
        D = biclock_D
    d = 0
    tmp = 0
    while True :
        nx,ny = x+D[d][0],y+D[d][1]
        if 0<=nx<R and 0<=ny<C:
            if G[nx][ny]==-1:
                break
            G[nx][ny],tmp = tmp,G[nx][ny]
            x,y = nx,ny
        else:
            d= (d+1)%4


for _ in range(T):
    G = expand(G)
    for i, (x,y) in enumerate(airs):
        air(x,y,i)

result = 0
for i in range(R):
    for j in range(C):
        if G[i][j]!= -1:
            result+=G[i][j]

print(result)


"""
2 3 50
-1 4 5
-1 4 6


7 8 50
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
0 0 -1 0 0 0 22 0
0 8 -1 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0


7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
0 0 5 0 0 0 22 0
0 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
-1 0 5 0 15 0 0 0
-1 0 40 0 0 0 20 0
"""