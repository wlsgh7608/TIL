"""
https://www.acmicpc.net/problem/1976
여행 가자 / 골드 4/ 50분
실패 4(런타임 에러4)
인덱스 에러가 나는 이유를 모르겠어서 힌트얻고 품
"""
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
travels = list(map(int,input().split()))
parent= [i for i in range(N)]



def find_parent(x):
    if parent[x]!= x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a] = b

for i in range(N):
    for j in range(N):
        if G[i][j] ==1:
            union(i,j)



set_list = set(parent[travel-1] for travel in travels)
if len(set_list)>1:
    print("NO")
else:
    print("YES")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0 
2 3 4 3

"""