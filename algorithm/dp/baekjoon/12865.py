"""
https://www.acmicpc.net/problem/12865
평범한 배낭 / 골드 5 / 14분 
9:31 ~ 9:45
"""
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
dp = [0 for _ in range(K+1)]
for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])