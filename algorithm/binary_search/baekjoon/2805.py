"""
https://www.acmicpc.net/problem/2805
나무 자르기 / 실버 3 / 30분
실패 3, 성공
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
trees = list(map(int,input().split()))

trees.sort()
lo,hi = 0,trees[-1]


# upper bound 이용
while lo<=hi:
    m = (lo+hi)//2
    tree_len = [tree-m for tree in trees if tree>m]
    tot = sum(tree_len)
    if tot >= M:
        lo = m + 1
    else:
        hi = m - 1
    
print(lo-1)
