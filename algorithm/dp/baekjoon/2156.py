"""
https://www.acmicpc.net/problem/2156
포도주 시식 / 실버 1 / 8분
9:21 ~ 9:29
"""
import sys
input = sys.stdin.readline


n = int(input())
grapes = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    if i < 2:
        dp[i] = dp[i-1] + grapes[i]
    else:
        dp[i] = max(dp[i-1],dp[i-2]+grapes[i], dp[i-3]+grapes[i-1]+grapes[i])
    
print(dp[-1])