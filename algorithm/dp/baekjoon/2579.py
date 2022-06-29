"""
https://www.acmicpc.net/problem/2579
계단 오르기 / 실버 3 / 15분
실패 1(런타임 에러)
9:05 ~ 9:20
"""
import sys
input = sys.stdin.readline

iter = int(input())
steps = [0]
for _ in range(iter):
    step = int(input())
    steps.append(step)

dp = [0 for _ in range(len(steps))]
dp[1] = steps[1]
if len(steps)>2:
    dp[2] = steps[1]+steps[2]
for i in range(3,len(steps)):
    two_step = dp[i-2] + steps[i] 
    one_step = dp[i-3] + steps[i-1] + steps[i]
    dp[i] = max(one_step,two_step)
print(dp[-1])