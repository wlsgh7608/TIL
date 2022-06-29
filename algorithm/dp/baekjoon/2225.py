"""
https://www.acmicpc.net/problem/2225
합분해 / 골드 5/ 23분 
15:15 ~ 15:38
"""
import sys
input = sys.stdin.readline
N,K = map(int,input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K)] 
dp[0] = [1 for _ in range(N+1)] # 초기화
for k in range(1,K):
    for i in range(N+1):
        for j in range(i+1):
            dp[k][i] += dp[k-1][i-j]

print(dp[-1][-1]%1_000_000_000)
