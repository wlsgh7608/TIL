"""
https://www.acmicpc.net/problem/1003
피보나치 함수 / 실버 3 / 5분
8:57 ~ 9:02

"""
import sys
input = sys.stdin.readline
dp = [[0,0] for _ in range(41)] # 0<=n<=40
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]


n = int(input())

for _ in range(n):
    number = int(input())
    print(*dp[number])
