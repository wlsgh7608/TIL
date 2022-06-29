"""
https://www.acmicpc.net/problem/10775
공항 / 골드 2 / 60분
실패2(틀렸습니다 1 , 시간초과 1 )
"""
import sys
input = sys.stdin.readlineㄴ


G = int(input())
P = int(input())
A = [int(input())for _ in range(P)]
parent  = [i for i in range(G+1)]

def find_parent(x):
    if parent[x]  != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a):
    a = find_parent(a)
    b = find_parent(a-1)
    if a==0:
        return False
    else:
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        return True
result = 0
for air in A:
    if not union(air):
        break
    result +=1
print(result)

