"""
https://www.acmicpc.net/problem/2887
행성 터널 / 골드 1 / 40분
실패 3 (메모리초과 3)
"""
import sys
input = sys.stdin.readline
N = int(input())
G=[]
for i in range(N):
    x,y,z = list(map(int,input().split()))
    G.append((x,y,z,i))
    
E = []


def find_parent(v):
    if parent[v]!=v:
        parent[v] = find_parent(parent[v])
    return parent[v]
def union(a,b):
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for k in range(3):
    G.sort(key=lambda x: x[k])
    for i in range(N-1):
        dist = abs(G[i][k] - G[i+1][k])
        a = G[i][3]
        b = G[i+1][3]
        E.append((dist,a,b))

        


parent = [i for i in range(N)]
E.sort()
result = 0
for v,a,b in E:
    r_a = find_parent(a)
    r_b =  find_parent(b)
    if r_a != r_b:
        union(r_a,r_b)
        result+=v
    
print(result)