"""
https://www.acmicpc.net/problem/14500

체크리스트
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
    - 현재 위치에서 만들 수 있는 테트로미노를 모두 계산
"""
def number_check(G,i,j,result):
    
    if i <= N-3 and j <= M-2:
        result = max(result,three_by_two(G,i,j))
    if i <= N-2 and j <= M-3 :
        result = max(result,two_by_three(G,i,j)) 
    if  j <= M-4 :
        result = max(result,one_by_four(G,i,j)) 
    if i <= N-4 :
        result = max(result,four_by_one(G,i,j)) 
    if i <= N-2 and j <= M-2 :
        result = max(result,two_by_two(G,i,j)) 
    return result

def two_by_three(G,i,j):
    max_n = 0
    sum = 0
    for x in range(i,i+2):
        for y in range(j,j+3):
            sum += G[x][y]
    max_n = max(max_n,sum-G[i][j]-G[i][j+1],sum-G[i][j+1]-G[i][j+2],sum-G[i+1][j]-G[i+1][j+1],sum-G[i+1][j+1]-G[i+1][j+2])
    max_n = max(max_n,sum-G[i][j]-G[i+1][j+2],sum-G[i][j+2]-G[i+1][j])
    max_n = max(max_n,sum-G[i][j]-G[i][j+2],sum-G[i+1][j]-G[i+1][j+2])
    return max_n
def three_by_two(G,i,j):
    max_n = 0
    sum = 0
    for x in range(i,i+3):
        for y in range(j,j+2):
            sum += G[x][y]
    max_n = max(max_n,sum-G[i][j]-G[i+1][j],sum-G[i+1][j]-G[i+2][j],sum-G[i][j+1]-G[i+1][j+1],sum-G[i+1][j+1]-G[i+2][j+1])
    max_n = max(max_n,sum-G[i][j]-G[i+2][j+1],sum-G[i+2][j]-G[i][j+1])
    max_n = max(max_n,sum-G[i][j]-G[i+2][j],sum-G[i][j+1]-G[i+2][j+1])
    return max_n
def two_by_two(G,i,j):
    sum = 0
    for x in range(i,i+2):
        for y in range(j,j+2):
            sum+=G[x][y]
    return sum
def one_by_four(G,i,j):
    sum = 0 
    for y in range(j,j+4):
        sum+= G[i][y]
    return sum
def four_by_one(G,i,j):
    sum = 0
    for x in range(i,i+4):
        sum+= G[x][j]
    return sum


N, M =  map(int,input().split())

G = []
for _ in range(N):
    inp = list(map(int,input().split()))
    G.append(inp)

max_n = 0
for i in range(N):
    for j in  range(M):
        max_n = number_check(G,i,j,max_n)

print(max_n)