"""
https://www.acmicpc.net/problem/11049
행렬 곱셈 순서 / 골드 3 / 50분
09:00 ~ 09:50
"""
import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
A = []
for _ in range(n):
    r,c = map(int,input().split())
    A.append((r,c))
dp = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
# dp[i][j] = i에서 j까지 연산할 때의 최소 연산
for  i in range(n-1,-1,-1):
    for j in range(i+1,n):
        dist = j-i
        for k in range(dist):
            dp[i][j] = min(dp[i][j],dp[i][i+k]+dp[i+k+1][j]+A[i][0]*A[i+k][1]*A[j][1])
print(dp[0][-1])