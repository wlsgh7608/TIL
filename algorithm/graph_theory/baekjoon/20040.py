"""
https://www.acmicpc.net/problem/20040
사이클 게임 / 골드 4 / 6분
실패1(런타임 에러1)
11:56
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def is_cycle_union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a !=b:
        parent[a] =b
        return False 
    return True
n,m  = map(int,input().split())
parent =[i for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    if is_cycle_union(a,b):
        print(i+1)
        break
else:
    print(0)

