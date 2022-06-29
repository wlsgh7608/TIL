"""
https://www.acmicpc.net/problem/3190
체크리스트
- [ ] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
    - 다음 갈 위치에 보드의 끝인지 뱀몸통이 있는지 확인 후 진행


"""

n = int(input()) # 보드
A = int(input()) # 사과
apples = set()
for _ in range(A):
    apples.add(tuple(map(int,input().split())))
L = int(input())
moves = []
for _ in range(L):
    s,d = input().split()
    if d == 'L':
        d = -1
    else:
        d = 1
    s = int(s)
    moves.append([s,d])
D = [(0,1),(1,0),(0,-1),(-1,0)]

snakes = []
t = 0
cur_d = 0
x,y = 1,1
while True:
    snakes.append((x,y))
    if moves and t == moves[0][0]: # 방향전환 정보
        cur_d = (cur_d+ moves[0][1])%4
        moves.pop(0)
    nx,ny = x+D[cur_d][0], y + D[cur_d][1]
    if nx and ny and nx<=n and ny<=n and (nx,ny) not in snakes : # 보드끝에 닿지 않고 뱀이 끝에 닫지 않는 경우
        if (nx,ny) in apples:
            d_set= set()
            d_set.add((nx,ny))
            apples = apples-d_set
        else:
            snakes.pop(0)
    else:
        t+=1 # 다음 진행에 부딪히므로 시간+1
        break
    
    x,y = nx,ny
    t+=1
print(t)
            



"""
check
6
4
1 2
2 1
2 2
1 1
4
1 R
2 R
3 R
4 R


check
6 
0
1
0 L


"""